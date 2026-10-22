#!/usr/bin/env python3
"""Explorador PRODES -- preenche o template com a tabulacao do mestre.

Sucede o gerar_explorador_v3_10m.py (16/10/2026). O HTML vem do
explorador_prodes_template.html (montado da pagina publicada pelo
montar_template_explorador_prodes.py); aqui so entram os dados, os testes e os
numeros do texto.

Os anos do PRODES:
  - na tabulacao, o 2024 esta no bit 7 da banda 1; o 2023 no bit 6 e o 2025 no
    bit 5 da banda 2;
  - a pagina move o 2024 para o bit 28 da banda 2 e faz do bit 7 da banda 1 o
    desmatamento DOS ANOS MARCADOS. Os testes daqui refazem essa mesma regra em
    pandas, de forma independente, para o ?validar comparar.

O recorte NAO vai na pagina: ela o tira do Brasil inteiro. Os testes do recorte
sao calculados sobre a tabulacao do RASTER do recorte, feita a parte -- entao o
?validar confere tambem que as duas tabulacoes contam a mesma mancha.
"""
import argparse, json, random, sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import schema as V3   # grupos, dimensoes e legenda vem dali

P = Path('/media/gr-dev/HD_2/projeto_raster_mestre')
# A pagina oficial e a aplicacao unica (Simplificada | Completa). Desde 22/10/2026
# o template canônico é versionado neste repositório; não depende de um commit antigo.
TEMPLATE_V1 = Path(__file__).resolve().parent / 'explorador_prodes_template.html'
TEMPLATE = Path(__file__).resolve().parents[1] / 'src' / 'explorador_prodes_template.html'
FLAGS_INFO = P / '2_BASE_FUNDIARIA/car_flags_10m.json'
ANOS = [(2023, 106), (2024, 128), (2025, 105)]   # ano -> bit onde a pagina o guarda
BIT_VIRTUAL = 7
FLORESTA = [3, 4, 5, 6, 7, 49]                       # grupos do explorador
HERBACEA = [11, 12, 29, 32, 50, 77, 84]


def grupos_bits():
    """Grupos de filtro da pagina: os do v3, com o bit 7 nos anos marcados.

    Funcao, e nao so dentro do main(), porque o gerar_camada_geodashboard.py
    le daqui os mesmos grupos (dentro de um grupo os filtros somam com OU).
    """
    grupos = [g for g in V3.GRUPOS_BITS if g[0] != 'Desmatamento']
    grupos.insert(0, ('Desmatamento PRODES', [(7, 'Desmatado nos anos marcados')]))
    return grupos


def dimensoes():
    """Dimensoes da pagina: as do v3, com o ano do PRODES e o vazio do CAR."""
    dims = json.loads(json.dumps(V3.DIMENSOES))
    dims['prodes'] = {'tipo': 'bits', 'rotulo': 'Ano do desmatamento PRODES',
                      'vazio': 'Não desmatado', 'bits': [[b, str(y)] for y, b in ANOS]}
    sem_mf = 0
    if FLAGS_INFO.exists():
        fi = json.loads(FLAGS_INFO.read_text())
        sem_mf = sum(r.get('sem_mod_fiscal', 0) for r in fi['por_uf'].values())
    dims['fundiario']['vazio'] = 'Fora do CAR'
    dims['tamanho']['vazio'] = 'Fora do CAR' if not sem_mf else 'Fora do CAR ou sem módulo fiscal'
    return dims


def remapeia(f, anos):
    """A regra da pagina: 2024 vai para o bit 28 da banda 2, e o bit 7 da
    banda 1 vira 'desmatado em algum dos anos marcados'."""
    v = f.valor.to_numpy().astype(np.int64)
    u = f.banda2.to_numpy().astype(np.int64)
    real24 = (v >> 7) & 1
    v = v & ~np.int64(1 << 7)
    u = u | (real24 << 28)
    m = 0
    for a, b in ANOS:
        if a in anos:
            m |= 1 << (b - 100)
    virt = (u & m) != 0
    v = v | (virt.astype(np.int64) << BIT_VIRTUAL)
    return v, u, virt


def casos_de_teste(tab_mestre, tab_recorte, grupos):
    BITS = ([7, 8, 9, 10, 11, 12, 13, 14, 15] + list(range(16, 28)) + [28, 29]
            + list(range(110, 122)) + [105, 106, 128, 108, 109])
    grupo_do_bit = {b: g for g, bs in grupos for b, _ in bs}
    random.seed(16102026)
    casos, cache = [], {}

    def uni(u, anos):
        k = (u, tuple(anos))
        if k not in cache:
            f = tab_mestre if u == 'mestre' else tab_recorte
            v, b2, virt = remapeia(f, anos)
            d = pd.DataFrame({'v': v, 'u': b2, 'a': f.area_ha.round(4).to_numpy(),
                              'cls': f.valor.to_numpy() & 127,
                              'uf': f.banda2.to_numpy() & 31})
            if u == 'recorte':
                d = d[virt].reset_index(drop=True)
            cache[k] = d
        return cache[k]

    def liga(d, b):
        if b >= 100:
            return ((d.u.to_numpy() >> (b - 100)) & 1) == 1
        return ((d.v.to_numpy() >> b) & 1) == 1

    def calc(u, anos, req, neg, cls, uf=None):
        d = uni(u, anos)
        m = np.ones(len(d), dtype=bool)
        porg = {}
        for b in req:
            porg.setdefault(grupo_do_bit.get(b, b), []).append(b)
        for bits in porg.values():
            acc = np.zeros(len(d), dtype=bool)
            for b in bits:
                acc |= liga(d, b)
            m &= acc
        for b in neg:
            m &= ~liga(d, b)
        if cls:
            m &= d.cls.isin(cls).to_numpy()
        if uf is not None:
            m &= d.uf.to_numpy() == (V3.UFS.index(uf) + 1)
        return float(d.a[m].sum()), int(m.sum())

    def caso(u, anos, req, neg, cls, uf=None):
        a, c = calc(u, anos, req, neg, cls, uf)
        x = {'u': u, 'anos': list(anos), 'req': req, 'neg': neg, 'cls': cls,
             'a': a, 'c': c}
        if uf:
            x['uf'] = uf
        casos.append(x)

    todos = [a for a, _ in ANOS]
    for anos in ([2023], [2024], [2025], todos):
        for u in ('mestre', 'recorte'):
            for b in BITS:
                caso(u, anos, [b], [], [])
        caso('recorte', anos, [], [], [])
    for b in BITS:
        caso('mestre', [2025], [], [b], [])
    for _ in range(40):
        req = random.sample(BITS, random.choice([2, 3]))
        neg = random.sample([b for b in BITS if b not in req], random.choice([0, 1, 2]))
        caso(random.choice(['mestre', 'recorte']), random.choice([[2023], [2024], [2025], todos]),
             req, neg, [])
    cls_disp = sorted(int(c) for c in (tab_mestre.valor & 127).unique())
    for _ in range(20):
        cs = random.sample(cls_disp, random.choice([1, 2, 3]))
        req = random.sample(BITS, random.choice([0, 1, 2]))
        caso('mestre', random.choice([[2023], [2024], [2025], todos]), req, [], cs)
    for uf in ['PA', 'MT', 'MA', 'BA', 'TO', 'MG', 'RS', 'AM']:
        for req in ([7], [7, 8], [7, 16], [7, 28], [7, 9], []):
            caso('mestre', [2025] if uf in ('PA', 'MA', 'TO', 'AM') else todos,
                 req, [], [], uf)
    return casos


def br(x, c=0):
    return f'{x:,.{c}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def main():
    global FLAGS_INFO
    ap = argparse.ArgumentParser()
    ap.add_argument('--mestre', default=str(P / 'A3_MESTRE_10M/tabelas/valores_v3_10m.csv'))
    ap.add_argument('--recorte', default=str(P / 'B3_SOMENTE_PRODES_10M/tabelas/valores_v3_10m.csv'))
    ap.add_argument('--saida', default=str(P / 'E3_EXPLORADOR_10M/documentos/explorador_prodes.html'))
    # Padrao: a pagina oficial (aplicacao unica). --template com o
    # explorador_prodes_template.html gera a v1 antiga, com os mesmos dados.
    ap.add_argument('--template', default=str(TEMPLATE))
    ap.add_argument('--legenda', default=str(V3.LEG))
    ap.add_argument('--flags', default=str(FLAGS_INFO))
    a = ap.parse_args()
    FLAGS_INFO = Path(a.flags)

    tm = pd.read_csv(a.mestre, usecols=['valor', 'banda2', 'area_ha'])
    tr = pd.read_csv(a.recorte, usecols=['valor', 'banda2', 'area_ha'])

    grupos = grupos_bits()
    dims = dimensoes()

    # mesmas guardas do v3: grupo so entra se o dado ja tiver os bits
    b2 = tm.banda2.to_numpy().astype('uint64')
    if not ((b2 >> np.uint64(8)) & np.uint64(0x3)).any():
        raise SystemExit('APP e RL ausentes da tabulação -- tabulação errada?')
    if not ((b2 >> np.uint64(22)) & np.uint64(0x3F)).any():
        raise SystemExit('sobreposição CAR x CAR ausente da tabulação')

    # numeros do texto, tirados da tabulacao do recorte
    v = tr.valor.to_numpy(); u = tr.banda2.to_numpy()
    d23 = ((u >> 6) & 1) == 1
    d24 = ((v >> 7) & 1) == 1
    d25 = ((u >> 5) & 1) == 1
    cls = v & 127
    veg = np.isin(cls, FLORESTA + HERBACEA)
    ha = tr.area_ha.to_numpy()
    ha23, ha24, ha25 = float(ha[d23].sum()), float(ha[d24].sum()), float(ha[d25].sum())
    pv23 = 100 * float(ha[d23 & veg].sum()) / ha23 if ha23 else 0
    pv24 = 100 * float(ha[d24 & veg].sum()) / ha24 if ha24 else 0
    pv25 = 100 * float(ha[d25 & veg].sum()) / ha25 if ha25 else 0
    nota_uso = (f'É o mesmo mapa para os três anos do PRODES: dois anos depois do '
                f'desmatamento de 2023, um depois do de 2024 e no mesmo ano do de 2025 — e o '
                f'mapa do mesmo ano nem sempre já mostra a supressão. Aparece ainda como '
                f'vegetação nativa (floresta ou herbácea) no MapBiomas 2025: '
                f'{br(pv23, 1)}% do desmatamento de 2023, {br(pv24, 1)}% do de 2024 e '
                f'{br(pv25, 1)}% do de 2025.')
    mais = (d23.astype(int) + d24.astype(int) + d25.astype(int)) > 1
    print(f'  2023: {ha23:,.0f} ha ({pv23:.1f}% como vegetação no MB 2025) | '
          f'2024: {ha24:,.0f} ha ({pv24:.1f}%) | 2025: {ha25:,.0f} ha ({pv25:.1f}%) | '
          f'em mais de um ano {float(ha[mais].sum()):,.1f} ha', flush=True)

    classes = {int(r.codigo): [r.nome, r.cor]
               for r in pd.read_csv(a.legenda).itertuples(index=False)}
    classes[0] = ['Fora do MapBiomas', '#efefef']
    dados = {
        'mestre': [[int(x), int(y), round(float(z), 4)]
                   for x, y, z in zip(tm.valor, tm.banda2, tm.area_ha)],
        'anos': [[y, b] for y, b in ANOS],
        'ufs': V3.UFS,
        'testes': casos_de_teste(tm, tr, grupos),
        'classes': classes,
        'grupos': [[g, [[b, r] for b, r in bs]] for g, bs in grupos],
        'grupo_do_bit': {str(b): g for g, bs in grupos for b, _ in bs},
        'dimensoes': dims,
    }
    html = Path(a.template).read_text(encoding='utf8')
    for k, val in {'__DATA__': date.today().strftime('%d/%m/%Y'),
                   '__HA2024__': br(ha24), '__NOTA_USO__': nota_uso}.items():
        # A v2 tirou o texto de abertura, onde iam a data e o total de 2024; o
        # template da v1 continua obrigado a ter os tres.
        if k not in html and Path(a.template).resolve() == TEMPLATE_V1.resolve():
            raise SystemExit(f'template sem {k}')
        html = html.replace(k, val)
    html = html.replace('__DADOS__', json.dumps(dados, ensure_ascii=False,
                                                separators=(',', ':')))
    saida = Path(a.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(html, encoding='utf8')
    print(f'{saida}\n  {saida.stat().st_size/1e6:.1f} MB | {len(tm):,} linhas | '
          f'{len(dados["testes"])} testes')


if __name__ == '__main__':
    main()
