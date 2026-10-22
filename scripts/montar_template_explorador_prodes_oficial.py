#!/usr/bin/env python3
"""Exporta o template canônico para ferramentas externas, sem patches antigos."""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--saida', type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / 'src' / 'explorador_prodes_template.html'
    template = source.read_text()
    if template.count('__DADOS__') != 1 or template.count('__NOTA_USO__') != 1:
        raise SystemExit('Template canônico inválido')
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_text(template)
    print(args.saida)


if __name__ == '__main__':
    main()
