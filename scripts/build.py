#!/usr/bin/env python3
"""Renderiza o template versionado, reutilizando ou substituindo os dados."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / 'src' / 'explorador_prodes_template.html'


def payload(html):
    match = re.search(r'^const D=(\{[^\n]+\});$', html, re.M)
    note = re.search(r'É o mesmo mapa para os três anos do PRODES.*?do de 2025\.', html, re.S)
    if not match or not note:
        raise ValueError('HTML sem os dados ou a nota de uso do solo esperados')
    return match[1], note[0]


def render(template, data, note):
    for marker in ('__DADOS__', '__NOTA_USO__'):
        if template.count(marker) != 1:
            raise ValueError(f'O template precisa conter exatamente um {marker}')
    values = {'__DADOS__': data, '__NOTA_USO__': note}
    return re.sub(r'__DADOS__|__NOTA_USO__', lambda match: values[match[0]], template)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--payload-from', type=Path, default=ROOT / 'index.html')
    parser.add_argument('--data', type=Path, help='JSON preparado pelo gerador de dados')
    parser.add_argument('--note', type=Path, help='Nota correspondente ao novo conjunto de dados')
    parser.add_argument('--output', type=Path, default=ROOT / 'index.html')
    parser.add_argument('--check', action='store_true', help='Confere sem escrever arquivos')
    args = parser.parse_args()
    if bool(args.data) != bool(args.note):
        parser.error('--data e --note devem ser informados juntos')
    if args.data:
        data = json.dumps(json.loads(args.data.read_text()), ensure_ascii=False, separators=(',', ':'))
        note = json.dumps(args.note.read_text().strip(), ensure_ascii=False)[1:-1]
    else:
        data, note = payload(args.payload_from.read_text())
    html = render(TEMPLATE.read_text(), data, note)
    if args.check:
        if not args.output.exists() or args.output.read_bytes() != html.encode():
            raise SystemExit('index.html diverge do template; execute python3 scripts/build.py')
        print('HTML idêntico ao template + dados, byte a byte.')
    else:
        args.output.write_text(html)
        print(args.output)


if __name__ == '__main__':
    main()
