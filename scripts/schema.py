"""Esquema original dos bits e dimensões; extraído do gerador v3, sem o HTML legado."""

from pathlib import Path

LEG = Path('/media/gr-dev/HD_2/projeto_raster_mestre/1_INSUMOS/legenda_mapbiomas_col11.csv')

UFS = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB',
       'PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']

GRUPOS_BITS = [
    ('Desmatamento', [(7, 'Desmatamento PRODES 2024')]),
    ('Cadastro', [(8, 'Dentro de imóvel do CAR')]),
    # Categoria do SNUC, banda 2 bits 10-21. Nem a v1 nem a v2 tinham isto:
    # elas paravam nos dois grupos, e somar APA com RESEX e RPPN escondia que
    # uma APA admite propriedade privada e ocupacao, e um Parque nao.
    ('Categoria da UC (SNUC)', [
                              (110, 'Estação Ecológica'),
                              (111, 'Reserva Biológica'),
                              (112, 'Parque'),
                              (113, 'Monumento Natural'),
                              (114, 'Refúgio de Vida Silvestre'),
                              (115, 'Área de Proteção Ambiental (APA)'),
                              (116, 'ARIE'),
                              (117, 'Floresta'),
                              (118, 'Reserva Extrativista'),
                              (119, 'Reserva de Fauna'),
                              (120, 'Reserva de Desenv. Sustentável'),
                              (121, 'RPPN')]),
    ('Aderência do CAR ao fundiário — SIGEF e SNCI separados',
     [(9, 'Aderente ao SIGEF (≥90%)'),
                                (10, 'Aderente ao SNCI (≥90%)'),
                                (11, 'Tem parcela, aderência <90%'),
                                (12, 'Sem parcela fundiária')]),
    ('Tamanho do imóvel', [(13, 'Pequena (≤4 MF)'), (14, 'Média (>4 e ≤15 MF)'),
                           (15, 'Grande (>15 MF)')]),
    ('Categorias territoriais', [
        (16, 'Terra Indígena'), (17, 'UC Federal + PI'), (18, 'UC Federal + US'),
        (19, 'UC Estadual + PI'), (20, 'UC Estadual + US'),
        (21, 'UC Municipal + PI'), (22, 'UC Municipal + US'),
        (23, 'Território Quilombola'), (24, 'Assentamento Federal'),
        (25, 'Assentamento Estadual'),
        (26, 'Floresta Pública Não Destinada Federal'),
        (27, 'Floresta Pública Não Destinada Estadual')]),
    ('Contorno da parcela — SIGEF e SNCI separados', [(28, 'Parcela SIGEF'),
                                      (29, 'Parcela SNCI privada')]),
    # Sobreposicao CAR x CAR, banda 2 bits 22-27 -> 122-127 aqui. DUAS leituras
    # da mesma decisao, e elas NAO se somam: a de area mede chao, a de imovel
    # mede alcance. Ver o texto de ajuda do grupo.
    # APP e Reserva Legal declaradas no CAR, banda 2 bits 8-9 -> 108-109.
    # Separadas de proposito: sao regimes juridicos diferentes, e medido que RL
    # responde por 92% a 95% do que esta protegido -- num bit so, APP sumiria.
    ('APP e Reserva Legal declaradas', [
        (108, 'Reserva Legal declarada'),
        (109, 'APP declarada')]),
    ('Sobreposição entre imóveis do CAR', [
        (122, 'Área sobreposta — ínfima (<1 ha e <10%)'),
        (123, 'Área sobreposta — sobreposição'),
        (124, 'Área sobreposta — aderente (≥90% nos dois sentidos)'),
        (125, 'Imóvel com sobreposição ínfima'),
        (126, 'Imóvel com sobreposição'),
        (127, 'Imóvel aderente a outro CAR')]),
]

DIMENSOES = {
    'mapbiomas': {'rotulo': 'Uso do solo (MapBiomas col. 4, 10 m)', 'tipo': 'classe'},
    'territorial': {'rotulo': 'Categoria territorial', 'tipo': 'bits',
                    'bits': [(8, 'CAR'),
                             (16, 'Terra Indígena'), (17, 'UC Federal + PI'),
                             (18, 'UC Federal + US'), (19, 'UC Estadual + PI'),
                             (20, 'UC Estadual + US'), (21, 'UC Municipal + PI'),
                             (22, 'UC Municipal + US'), (23, 'Quilombola'),
                             (24, 'Assentamento Federal'),
                             (25, 'Assentamento Estadual'),
                             (26, 'Não Destinada Federal'),
                             (27, 'Não Destinada Estadual')]},
    'fundiario': {'rotulo': 'Aderência do CAR ao fundiário — SIGEF e SNCI separados',
                  'tipo': 'bits',
                  'vazio': 'Não avaliado',
                  'bits': [(9, 'CAR adere ao SIGEF (≥90%)'),
                           (10, 'CAR adere ao SNCI (≥90%)'),
                           (11, 'Tem parcela, mas <90%'),
                           (12, 'Sem parcela nenhuma')]},
    'tamanho': {'tipo': 'bits', 'rotulo': 'Tamanho do imóvel',
                'vazio': 'Não avaliado',
                'bits': [(13, 'Pequena'), (14, 'Média'), (15, 'Grande')]},
    'parcela': {'tipo': 'bits',
                'rotulo': 'Contorno da parcela — SIGEF e SNCI separados',
                'bits': [(28, 'Parcela SIGEF'), (29, 'Parcela SNCI privada')]},
    'car': {'tipo': 'bits', 'rotulo': 'CAR (filtrado)', 'bits': [(8, 'Em CAR')]},
    'app_rl': {'tipo': 'bits', 'rotulo': 'APP e Reserva Legal declaradas',
               'vazio': 'Fora de APP e de RL',
               'bits': [(108, 'Reserva Legal'), (109, 'APP')]},
    'sobrep_area': {'tipo': 'bits',
                    'rotulo': 'Sobreposição CAR × CAR — área sobreposta',
                    'vazio': 'Sem sobreposição',
                    'bits': [(122, 'Ínfima'), (123, 'Sobreposição'),
                             (124, 'Aderente (≥90%)')]},
    'sobrep_imovel': {'tipo': 'bits',
                      'rotulo': 'Sobreposição CAR × CAR — imóvel inteiro',
                      'vazio': 'Sem sobreposição',
                      'bits': [(125, 'Imóvel com ínfima'),
                               (126, 'Imóvel com sobreposição'),
                               (127, 'Imóvel aderente a outro CAR')]},
    'categoria_uc': {'tipo': 'bits', 'rotulo': 'Categoria da UC (SNUC)',
                     'vazio': 'Fora de UC',
                     'bits': [
                              (110, 'Estação Ecológica'),
                              (111, 'Reserva Biológica'),
                              (112, 'Parque'),
                              (113, 'Monumento Natural'),
                              (114, 'Refúgio de Vida Silvestre'),
                              (115, 'Área de Proteção Ambiental (APA)'),
                              (116, 'ARIE'),
                              (117, 'Floresta'),
                              (118, 'Reserva Extrativista'),
                              (119, 'Reserva de Fauna'),
                              (120, 'Reserva de Desenv. Sustentável'),
                              (121, 'RPPN')]},
    'prodes': {'tipo': 'bits', 'rotulo': 'Desmatamento 2024',
               'bits': [(7, 'Desmatado em 2024')]},
}
