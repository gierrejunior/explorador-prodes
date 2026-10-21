# FGV Agro - Plataforma Análise Territorial

Explorador PRODES: página única, autocontida, para explorar o desmatamento apontado pelo PRODES em
**2023, 2024 e 2025** cruzado com CAR, base fundiária SIGEF/SNCI, categorias territoriais,
categoria de unidade de conservação, tamanho do imóvel em módulos fiscais e uso
do solo pelo MapBiomas — **na grade de 10 metros**, com recorte por estado.

**Abrir:** https://gierrejunior.github.io/explorador-prodes/

O endereço antigo (`/explorador-prodes-2024/`) redireciona para este, com os
filtros junto. Link sem o ano abre no PRODES 2024, que era o único ano da
página antiga.

Acrescente `?validar` ao endereço para a página conferir a si mesma: ela refaz
em JavaScript as combinações calculadas em pandas e mostra o placar.

## Seleção rápida e painéis compactos de 21/10/2026

- Cada filtro da barra tem uma caixa para **incluir todas → excluir todas →
  limpar**; a seta separada abre o painel sem alterar a seleção. Seleção parcial
  aparece com ±; exclusão, com − em laranja. Os botões extras “Excluir” saíram.
- O mesmo ciclo vale para grupos e classes de uso do solo; as exclusões entram
  nos cálculos, nos caches, na troca de modo e no link compartilhado (`cn`).
- Opções em lista vertical: grupos primeiro, depois itens isolados; ambos em
  ordem alfabética em português, inclusive as opções dentro de cada grupo.
- Painéis mais estreitos, menos preenchimento e bordas internas removidas.
  Os detalhes usam só o triângulo; no celular os alvos de toque continuam maiores.
  A contagem de opções não ocupa espaço nos títulos dos grupos e “Fechar” fica
  centralizado verticalmente com o título do painel.
- No computador os sete tipos de gráfico ficam numa única barra contínua,
  sem a divisão visual entre opções principais e adicionais. No celular as
  opções adicionais permanecem em “Mais gráficos”.

## Correção de foco e acesso aos gráficos de 21/10/2026

- Alternar entre **Simplificado** e **Detalhado** preserva a seleção no gráfico,
  incluindo seleções de múltiplas comparações e categorias que só existem no
  Detalhado. A seleção guarda a definição e o modo em que foi feita; uma UC
  federal selecionada não se transforma no total de todas as UCs ao simplificar.
- O painel mantém a área exata e identifica a origem da seleção. O gráfico
  destaca as categorias atuais que contêm a seleção preservada. Limpar ou
  escolher uma nova seleção continua disponível normalmente.
- **Aplicar seleção como filtro** usa o recorte original. A seleção preservada
  também entra no link copiado (`fs`), permitindo reabrir a mesma análise.
- Todos os tipos de gráfico aparecem diretamente no computador. O controle
  **Mais gráficos** só aparece até 700 px de largura; redimensionar a janela
  atualiza o comportamento e escolher um gráfico no computador não oculta os demais.

## Revisão da experiência de análise de 21/10/2026

- **Simplificado / Detalhado** substituem Simplificada / Completa. A abertura
  sem parâmetros usa barras, uma comparação e classes agrupadas. No celular,
  as configurações começam recolhidas e a exportação fica depois do gráfico.
- O seletor de anos aparece no topo apenas em **Desmatamento PRODES**.
  Em **Brasil inteiro**, fica em **Configurar análise** quando há uma comparação
  por ano, filtro de desmatamento ou gráfico de percentual desmatado.
- A barra do Detalhado tem o título **Filtros** e mantém os assuntos agrupados.
  Em telas largas, os nove controles ocupam uma linha; em telas menores,
  quebram linha sem cortar os nomes. No computador, cada
  painel abre a 8 px do botão que o acionou, com ajuste às bordas da janela,
  fechamento por Escape ou clique fora e relação acessível entre botão e painel.
  No celular, o painel abre imediatamente abaixo do respectivo botão.
- Grupos de opções territoriais, categorias de UC e sobreposição seguem o mesmo
  ciclo das suas opções: **incluir → excluir → limpar**. Exclusão aparece em
  laranja com **−**. Os botões separados de exclusão foram removidos. Abrir os detalhes não altera
  a seleção. Grupos e classes de uso do solo também seguem os três estados.
- **Filtros aplicados** apresenta etiquetas removíveis, inclusive quando o painel
  está fechado ou o usuário muda para o modo Simplificado.
- A troca de modo preserva os filtros e a área selecionada. Os filtros guardam
  sua origem (`q` nos filtros pelo gráfico e `eb` para as opções), permitindo
  consultar os bits detalhados ou as classes agrupadas sem alargar o recorte.
  Os links compartilham essa origem. Comparações indisponíveis no Simplificado
  são adaptadas com uma mensagem apenas quando há mudança de comparação.
  A confirmação genérica de preservação não ocupa uma faixa; a origem da seleção
  fica nos detalhes do relatório, e seu recorte é mantido.
- A leitura de combinações usa um seletor com explicação. Os rótulos distinguem
  **Somente imóvel no CAR** de **Imóvel no CAR (inclui combinações)**. Os nomes
  de apresentação foram revisados também nas tabelas, legendas e exportações;
  as identidades internas dos filtros e das classes foram preservadas.
- “Floresta” aparece como **Formações florestais e savânicas**. O antigo grupo de
  vegetação herbácea passa a **Formações campestres, arbustivas e áreas úmidas**;
  **Afloramentos rochosos** ficam separados. O restante dos grupos conserva sua
  posição para manter os identificadores da calculadora.
- A área analisada tem um cartão compacto com borda verde, rótulo e número
  maior; os demais indicadores têm largura conforme o conteúdo. Configuração, gráficos e
  exportação ficam sem uma moldura larga; as ações da seleção aparecem junto
  do resultado, reduzindo espaços vazios sem esconder controles.
- O relatório da seleção começa recolhido. A área total e as ações de aplicar
  ou limpar continuam visíveis; **Ver relatório da seleção** abre a tabela,
  as condições e as explicações. A escolha de abrir é mantida durante a análise.
- Marcas dos gráficos e linhas da tabela podem ser selecionadas pelo teclado.
  Enter/Espaço selecionam; Shift+Enter aplica como filtro no gráfico. Controles
  de ajuda têm alvos maiores. Todos os tipos de gráfico ficam visíveis no computador;
  **Mais gráficos** reúne as opções adicionais apenas no celular.

Validação: 472/472 contagens e áreas, 60/60 conservações e 78/78 verificações
existentes de classes e nomes. Testes de navegador cobriram os três estados do
conjunto e dos filhos, posição do painel, preservação entre modos e por link,
links antigos, teclado, CSV/PNG e celular sem rolagem horizontal da página.

## Revisão de filtros de 21/10/2026

- A gaveta redundante de desmatamento saiu. O recorte continua disponível em
  **Universo → Desmatamento PRODES**.
- Os títulos explicam o objeto do filtro: **Área do imóvel no CAR**,
  **Correspondência CAR × SIGEF/SNCI**, **Áreas cadastradas no SIGEF/SNCI**,
  **Tipo de área ou território** e **Uso e cobertura do solo**. As opções
  explicitam módulos fiscais, proteção integral, uso sustentável e outras siglas.
- Nos subgrupos, clicar no **nome** seleciona todas as opções; clicar novamente
  exclui todas e o terceiro clique limpa o filtro. **Detalhar** abre as opções sem mudar o filtro. O cabeçalho
  mostra seleção parcial e exclusões, inclusive quando os detalhes estão fechados.
- O padrão vale para **Unidades de conservação**, **Assentamentos** e
  **Florestas públicas não destinadas**; também para os grupos de categorias de
  UC, as duas leituras da sobreposição CAR e os grupos do uso e cobertura do solo
  no nível detalhado. As opções individuais continuam disponíveis.
- O agrupamento só organiza os controles: dentro de uma gaveta as inclusões
  continuam com **ou**; entre gavetas, com **e**. Links existentes conservam os
  identificadores dos filtros e os nomes internos das categorias do gráfico.

## Atualização de 21/10/2026: uma aplicação, duas leituras

No topo da página, **Aplicação: Simplificada | Completa**. É um endereço só —
o `/v2/`, onde a versão simplificada foi testada, saiu.

- **Simplificada** (abre por padrão): para quem não acompanhou a construção dos
  dados. Classes agrupadas — SIGEF e SNCI como **base do INCRA**, aderência em
  **aderente (≥90%)** ou **não aderente**, UC só em **proteção integral** e
  **uso sustentável** (federais, estaduais e municipais juntas), **assentamentos**
  e **áreas não destinadas** sem separar federal e estadual, **RL e APP** numa
  classe, e a **sobreposição entre CARs** pelo chão sobreposto: fora do CAR, CAR
  sem sobreposição (os encostos mínimos entre vizinhos contam aqui), CAR
  sobreposto a outro e CAR duplicado. Sem filtros por categoria nem calculadora:
  filtra-se pelo próprio gráfico.
- **Completa**: a página de antes, com todas as classes, os filtros por
  categoria — agora numa **barra de gavetas** acima do gráfico: cada botão abre
  a sua embaixo da barra e mostra quantos filtros dela estão ligados; o gráfico
  fica com a largura inteira — e a calculadora, agora **calculadora de áreas em
  comum** ("sobreposição" ficou só para dois CARs no mesmo chão).
- Os dados são os mesmos nas duas; muda só o agrupamento. Trocar de aplicação
  recomeça filtros e destaque, porque as classes de uma não existem na outra.
- **Copiar link** leva a aplicação (`modo=simples` ou `modo=det`). Link de antes,
  sem ela, abre na Completa, com os mesmos filtros.
- Para os números não serem lidos errado, nas duas: cada porcentagem diz de que
  total é ("do Brasil inteiro", "do desmatamento de 2025"…, nunca "da
  seleção"); o **Em foco** é uma tabela (cada categoria, o resultado e o peso de
  uma na outra); e **Filtrar por isto** pergunta, com a área de cada escolha, se
  as combinações entram ("Terra Indígena" sozinha ou também "CAR + Terra
  Indígena").
- **Nomes únicos entre comparações.** O Em foco acha a categoria pelo nome, e
  "Floresta" era categoria de UC e grupo do uso do solo: clicar na Floresta do
  uso do solo (334.793 ha no desmatamento de 2025) mostrava a das UCs
  (6.524 ha). A categoria de UC passou a se chamar **Floresta (Nacional,
  Estadual ou Municipal)**, e os "Nenhum" ganharam nome ("Sem categoria
  territorial", "Sem parcela SIGEF/SNCI", "Fora do CAR"). O `?validar` confere.
- Os nomes das classes de sobreposição entre CARs ainda podem mudar.

## Correção de 21/10/2026: eixo do ano com um ano só

- O eixo **Ano do desmatamento PRODES** fica disponível no Desmatamento PRODES
  também com um ano só marcado — por exemplo, para o "2023" ser a primeira
  coluna do Sankey. Antes ele sumia nesse caso, e quem separava por ano com dois
  anos marcados e desmarcava um via a caixa da comparação mostrar outro eixo
  enquanto a conta continuava separando por ano. Os números nunca estiveram
  errados; a tela é que dizia um eixo e mostrava outro.

## Atualização de 16/10/2026: PRODES 2023, 2024 e 2025

- **Três anos do PRODES.** Clicando em **Desmatamento PRODES**, no quadro
  Universo, aparecem os anos: um, ou mais de um somados. No Brasil inteiro eles
  aparecem quando o filtro de desmatamento está ligado ou no % desmatado — só
  onde o ano entra na conta. Os anos não se sobrepõem: o PRODES marca cada pixel uma vez só
  (46 pixels, 0,5 ha, caem em dois anos na rasterização).
- **Uma versão só do INPE.** Os três anos vêm das camadas anuais publicadas
  entre julho e outubro de 2026. Essa versão revisou o 2024 de 1.957.066 para
  1.954.281 ha (−0,14%), quase tudo na Caatinga.
- **Aderência e tamanho para todo o CAR.** Antes só existiam para os 267 mil
  imóveis que cruzavam o desmatamento de 2024; agora valem para os 8,27 milhões
  de imóveis do CAR filtrado. No Brasil inteiro, aderência e tamanho passam a
  ter leitura própria, e o % desmatado funciona nesses dois eixos.
- **PRODES 2026 fica de fora** até sair para os seis biomas. Hoje só há o
  Cerrado completo e as áreas prioritárias da Amazônia (estimativa preliminar).
- **Uso do solo:** o mesmo MapBiomas 2025 para os três anos — dois anos depois
  do desmatamento de 2023, um depois do de 2024 e no mesmo ano do de 2025. O
  mapa do mesmo ano nem sempre já mostra a supressão: aparece ainda como
  vegetação nativa 15,8% do desmatamento de 2023, 22,4% do de 2024 e 25,8% do
  de 2025.

## O que mudou da versão de 30 m para a de 10 m

| | antes (30 m) | agora (10 m) |
|---|---|---|
| resolução | 30 m | **10 m**, nove vezes mais pixels |
| uso do solo | MapBiomas Coleção 11 | **Coleção 4**, a única disponível a 10 m |
| CAR | inteiro | **filtrado**: imóvel rural, cadastro ativo ou pendente, não cancelado |
| aderência ao fundiário | medida por **parcela** | medida por **imóvel**, com as parcelas dissolvidas |
| unidade de conservação | esfera × grupo | **mais as 12 categorias do SNUC** |

**Saiu desta versão:** parcela SNCI pública. **APP e Reserva Legal** declaradas
no CAR voltaram, junto com a **sobreposição entre imóveis do CAR** — em duas
leituras que não se somam: a área sobreposta mede o chão; o imóvel com
sobreposição mede o imóvel inteiro.

O filtro do CAR mantém 8.268.132 de 8.349.966 imóveis, 99,0% dos registros — mas remove assentamentos e territórios tradicionais, que concentram desmatamento. É por isso que a parcela do desmatamento "dentro do CAR" cai em relação à versão anterior.

## Números principais (hectares; % do desmatamento do ano)

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| **Desmatamento PRODES** | **2.413.338** | **1.954.281** | **1.563.342** |
| Dentro de imóvel do CAR | 1.863.879 (77,2%) | 1.496.789 (76,6%) | 1.191.056 (76,2%) |
| Em alguma das doze categorias territoriais | 578.914 (24,0%) | 451.688 (23,1%) | 361.575 (23,1%) |
| Imóvel adere ao SIGEF (≥90% nos dois sentidos) | 592.622 (24,6%) | 456.523 (23,4%) | 390.525 (25,0%) |
| Imóvel adere ao SNCI | 128.475 (5,3%) | 87.728 (4,5%) | 69.210 (4,4%) |
| Tem parcela sobreposta, mas abaixo de 90% | 394.321 (16,3%) | 288.739 (14,8%) | 259.725 (16,6%) |
| Sem parcela fundiária | 911.952 (37,8%) | 796.229 (40,7%) | 627.620 (40,1%) |
| Imóvel pequeno (até 4 módulos fiscais) | 592.745 (24,6%) | 525.665 (26,9%) | 355.666 (22,8%) |
| Imóvel médio (mais de 4 e até 15) | 488.579 (20,2%) | 375.485 (19,2%) | 307.741 (19,7%) |
| Imóvel grande (mais de 15) | 910.756 (37,7%) | 706.941 (36,2%) | 622.824 (39,8%) |
| Reserva Legal declarada | 372.605 (15,4%) | 318.411 (16,3%) | 278.954 (17,8%) |
| APP declarada | 35.608 (1,5%) | 26.704 (1,4%) | 20.097 (1,3%) |

As categorias se sobrepõem de propósito: o raster não embute regra de
atribuição, então somar linhas dá mais que o total.

### Desmatamento em unidade de conservação

As duas tabelas descrevem **as mesmas** unidades por dois critérios distintos —
a categoria do SNUC e a esfera administrativa combinada com o grupo de manejo —
e portanto não se somam entre si.

Por categoria do SNUC:

| categoria | 2023 | 2024 | 2025 |
|---|---|---|---|
| Área de Proteção Ambiental | 111.930 | 77.541 | 57.372 |
| Reserva Extrativista | 12.335 | 10.331 | 5.861 |
| Floresta | 10.889 | 7.180 | 6.524 |
| Parque | 7.175 | 4.492 | 2.356 |
| Estação Ecológica | 10.483 | 4.241 | 1.630 |
| Reserva de Desenvolvimento Sustentável | 990 | 2.095 | 1.886 |
| Reserva Biológica | 670 | 1.023 | 1.900 |
| Refúgio de Vida Silvestre | 637 | 815 | 385 |
| Reserva Particular do Patrimônio Natural | 132 | 173 | 114 |
| Monumento Natural | 397 | 161 | 126 |
| Área de Relevante Interesse Ecológico | 145 | 26 | 54 |

Por esfera e grupo de manejo (US = uso sustentável, PI = proteção integral):

| esfera e grupo | 2023 | 2024 | 2025 |
|---|---|---|---|
| Estadual + US | 94.327 | 58.451 | 50.299 |
| Federal + US | 36.034 | 36.467 | 20.508 |
| Estadual + PI | 14.691 | 6.685 | 2.263 |
| Federal + PI | 4.672 | 4.018 | 4.108 |
| Municipal + US | 6.384 | 2.865 | 1.462 |
| Municipal + PI | 30 | 30 | 27 |

## Por que a aderência caiu em relação à versão anterior

Medir a aderência por **imóvel** em vez de por **parcela** parecia só uma
correção: um imóvel do CAR composto de várias parcelas reprovava no critério
porque cada parcela cobria só uma fração dele.

A correção funcionou — **114.618 imóveis** passaram a aderir. Mas ela também
quebrou o caso oposto: ao fundir parcelas, o imóvel fundiário fica maior e passa
a cobrir **vários** imóveis do CAR, e aí reprova no sentido inverso. Foram
**262.711 imóveis** perdidos por isso.

O saldo é uma queda de **20,4%**. O critério de 90% **nos dois sentidos** não é
invariante à unidade de agregação: as duas medições são enviesadas, em direções
opostas. Quem comparar os números das duas versões vai ver essa diferença, e ela
é metodológica, não um erro de uma delas.

## Como ler

Na aplicação Completa, as gavetas acima do gráfico **filtram** o que entra na
conta; em **Separar por** você **separa** o que entrou. Dentro de um mesmo grupo
os filtros somam com **ou**; entre grupos, com **e**. Nas duas aplicações dá
para filtrar pelo próprio gráfico (abaixo). A frase acima dos números descreve
sempre o que está na tela.

Cada comparação tem o próprio botão de leitura, com três estados, que decide
como contar um pixel que pertence a mais de uma classe daquela comparação:

| | o que você vê | soma |
|---|---|---|
| **cada combinação** | "Pequena + Grande" aparece separada de "Grande" — mostra QUAIS se sobrepõem | fecha com o total |
| **combinações juntas** | todo pixel em mais de uma classe vira "Mais de uma categoria" — mostra QUANTO há | fecha com o total |
| **total por classe** | "Grande" já inclui o que divide pixel com "Pequena" — mostra QUANTO há de cada classe | passa do total, de propósito |

A **ordem** das comparações decide o que é nível 1 e nível 2 (ou a primeira
coluna do Sankey). Para trocar, arraste pela alça **⠿** ao lado do número — com
mouse ou com o dedo — e solte em cima da comparação cujo lugar ela deve ocupar;
no teclado, as setas ↑ ↓ sobre a alça fazem o mesmo. Cada comparação leva junto
o próprio modo de leitura. Os números são os mesmos de ter escolhido as
comparações nessa ordem; destaque e filtros continuam valendo, e o link copiado
sai na ordem nova.

Há botões **ⓘ** espalhados pelos controles explicando cada um. O botão
**Baixar PNG** salva o gráfico como está na tela.

No Sankey toda comparação é separada, por imposição do próprio gráfico: ele
precisa que o que sai de uma coluna seja exatamente o que entra na seguinte.

O **uso do solo** abre agrupado nos oito grupos definidos pelo time; o botão
**Detalhado**, no filtro e na comparação de uso do solo, volta às classes do
MapBiomas. Trocar de nível não muda a conta: os hectares de um grupo são a soma
exata das suas classes.

| grupo | classes do MapBiomas (códigos) |
|---|---|
| Floresta | Formação Florestal, Floresta Alagável, Formação Savânica, Savana Alagada, Mangue, Restinga Arbórea (3, 6, 4, 7, 5, 49) |
| Vegetação herbácea | Formação Campestre, Formação Herbáceo Arbustiva, Campo Alagado e Área Pantanosa, Marisma, Restinga Herbácea ou Arbustiva, Apicum, Afloramento Rochoso (12, 77, 11, 84, 50, 32, 29) |
| Pastagem | Pastagem (15) |
| Agricultura anual | Lavoura Temporária (19) e as culturas temporárias da coleção 11 (39, 20, 40, 62, 41) |
| Agricultura perene | Lavoura Perene (36) e as culturas perenes da coleção 11 (46, 47, 35, 48) |
| Silvicultura | Silvicultura (9) |
| Mosaico de usos agro | Mosaico de Usos (21) |
| Outros | Praia, Duna e Areal, Área Urbanizada, Mineração, Usina Fotovoltaica, Parque Eólico, Outras Áreas não Vegetadas, Rio, Lago e Oceano, Aquicultura (23, 24, 30, 75, 91, 25, 33, 31) |

A grade de 10 m não separa as culturas: a agricultura vem só como Lavoura
Temporária e Lavoura Perene, por isso os códigos 19 e 36 entram nos grupos.
**Fora do MapBiomas** (código 0, sem classificação) fica à parte, com o
próprio nome. Links copiados antes desta opção abrem no detalhado, como eram.

Além de treemap, sunburst, pizza e Sankey, há três gráficos:

- **Barras** — uma barra por categoria da comparação 1, dividida pela
  comparação 2, em hectares ou em 100% (para comparar a composição). É o mais
  fácil de ler: comprimento se compara melhor que área ou ângulo.
- **Combinações** — cada coluna é uma combinação de categorias da
  comparação 1 (as bolinhas dizem quais estão juntas no mesmo pixel; a barra,
  quantos hectares). À esquerda, o total de cada categoria, contando também as
  combinações em que ela aparece.
- **% desmatado** — quanto de cada categoria da comparação 1 foi desmatado nos
  anos marcados: área desmatada ÷ área total da categoria, sempre sobre o
  Brasil inteiro, com os filtros escolhidos menos o de desmatamento.

A **calculadora de áreas em comum** (aplicação Completa) recebe categorias de qualquer grupo — inclusive
o **uso do solo**, no nível escolhido em Agrupado/Detalhado (duas classes de uso
do solo nunca se sobrepõem: cada pixel tem uma só) e mostra,
com os nomes escolhidos: a área ocupada por elas juntas (a união, cada hectare
uma vez — o número para citar), a área que é de todas ao mesmo tempo (a
interseção), a área que seria contada duas vezes se as áreas fossem somadas
separadamente, a área só delas sem outra categoria dos mesmos grupos, e como a
área ocupada se divide. A calculadora começa apenas com a instrução e o seletor
**Adicionar categoria**, sem comparações sugeridas.

**Destacar e filtrar.** São duas coisas, cada uma com seu lugar:

- **Clique** destaca: acende a parte clicada e apaga o resto, sem mudar a
  página. Dá para destacar várias; o resultado aparece no **Em foco**, logo
  acima do gráfico.
- **Filtrar por isto** (botão do Em foco) ou **duplo clique** filtram: a página
  inteira (cartões, gráfico, tabela, calculadora) passa a ser só aquilo, com um
  zoom curto partindo da parte escolhida. O filtro vira um passo da **trilha**
  acima do gráfico — `Brasil inteiro › Em CAR e Floresta › CAR + Terra Indígena`
  —, com **← voltar** e cada passo clicável para voltar direto a ele; o destaque
  esvazia ao filtrar, para a mesma coisa nunca estar nos dois lugares. Ao
  voltar, a tela volta como estava, com o destaque de antes de filtrar (se o
  filtro foi por duplo clique, acende o que foi filtrado); isso também vai no
  link.

Cada passo acumula com E sobre os anteriores; dentro de um passo, nomes da
mesma comparação somam com OU. O filtro é pelo rótulo exato — "CAR + Terra
Indígena" filtra só essa combinação —; no uso do solo, ele estreita o filtro de
uso do solo da esquerda. As porcentagens do destaque dizem sobre o quê são:
"1,8% de “Em CAR e Floresta”" dentro de um filtro, "da seleção" fora dele. A
trilha entra no link copiado; "Limpar todos os filtros" também a tira. O zoom não
muda o PNG e some para quem pede "reduzir movimento" no sistema.

**Destacar** segue a mesma regra de acumular: destacar "Sem parcela nenhuma" e
"Pastagem" acende só a Pastagem que está em Sem parcela e dá a conta desse
caminho (294.593 ha no desmatamento de 2024). No Sankey de três ou mais colunas
o destaque atravessa todas elas: o fluxo do Sankey só sabe o par de colunas
vizinhas, então a parte de cada fluxo que pertence ao caminho é recalculada nas
linhas e desenhada por cima, com a largura certa.

**Foco.** Clicar numa parte do gráfico ou num item da legenda destaca aquele
nome e apaga o resto: nas barras, a mesma categoria acende em todas as barras;
no Sankey, só os fluxos que saem ou chegam ao nó; no gráfico de sobreposições,
as colunas que contêm a categoria. Clicando em mais de um, todos ficam em foco.
Acima do gráfico aparecem o total de cada um e a área das escolhidas **juntas**
(cada hectare uma vez). A sobreposição aparece sempre, também quando é zero
("Sobreposição: 0 ha"), para não se confundir com conta que não foi feita; a
conta inteira fica em "ver o total de cada um": soma simples − sobreposição =
juntas; com duas, também "só A · nas duas · só B".

**Tabela e destaque são a mesma coisa.** Clicar numa linha da tabela põe o nome
no Em foco (o gráfico acende), e destacar no gráfico marca a linha (✓). A linha
"Σ em foco" traz o mesmo número do Em foco — cada hectare uma vez, mesmo com a
comparação em "total por classe", em que as linhas se sobrepõem — e embaixo dela,
a sobreposição. Como faz parte do foco, as linhas marcadas entram no link
copiado. Clicar no Σ limpa. Com a comparação em "cada combinação" e um eixo que
admite mais de uma categoria por pixel, a tabela diz também quando a
sobreposição é 0 ha.
A conta é feita direto nos dados, como a da calculadora, então vale também com
comparação em "somado". Os números mostrados fecham entre si: a soma é a dos
valores arredondados de cada um. Passar o
mouse na legenda mostra uma prévia; Esc ou "limpar foco" desfaz. O foco entra
no link copiado e no PNG: com foco ligado, a imagem sai como a tela (o resto
apagado) e com um rodapé "Em foco" que traz o total de cada item e o "Juntas";
sem foco, o PNG é o gráfico inteiro, como sempre.

No tema escuro a moldura ganha um brilho leve (bordas, cartões, botão ativo) e o
que está em foco brilha; no claro, vira uma sombra discreta. As cores dos dados
não mudam. Ao trocar filtro ou gráfico, cada gráfico entra do seu jeito: as
barras crescem; no Sankey os nós crescem e os fluxos se desenham da esquerda
para a direita, coluna por coluna; sunburst e pizza se revelam num giro a partir
do topo; o treemap surge com um zoom curto. Os números aparecem só no fim, já
com o valor final; quem pede "reduzir movimento" no sistema não vê animação.

**Cores.** Cada categoria tem cor fixa: a mesma em qualquer filtro, estado ou
gráfico. O uso do solo usa sempre as cores do MapBiomas — o verde fica só para
vegetação; o vermelho-alaranjado, só para o desmatamento; ausência ("Nenhum",
"Fora do CAR", "Fora de UC") é cinza claro. As demais categorias usam seis
cores sem verde e sem vermelho, escolhidas para continuarem distintas entre si
em qualquer par para quem tem daltonismo; onde há mais categorias que cores, a
mesma cor em tons diferentes marca o que é do mesmo tipo (UC de proteção
integral, UC de uso sustentável, assentamentos). Uma combinação, como
"CAR + Terra Indígena", aparece listrada com as cores das categorias que a
formam.

O seletor **Tema**, no alto da página, escolhe claro, escuro ou automático — o
automático segue o modo claro ou escuro do computador ou do celular.

## Método

Grade de **10 m**, atribuição pelo **centro do pixel**. Área
calculada por linha de latitude em EPSG:6933 — não por área fixa de pixel, que
erraria −17,4% no extremo sul.

A aderência exige **90% nos dois sentidos**: o imóvel do CAR coberto pela
parcela certificada e a parcela coberta pelo imóvel. Só assim as duas geometrias
descrevem o mesmo chão.

O CAR é autodeclaratório e tem imóveis sobrepostos entre si — **86,5 milhões de
hectares** de sobreposição no país. Somar área de imóvel conta esse chão mais de
uma vez; o raster não, porque conta o pixel uma vez.

**Aderência e tamanho** valem para todo imóvel do CAR filtrado (desde
16/10/2026). Fora do CAR eles estão apagados — "Fora do CAR" no gráfico.

O ano PRODES vai de agosto a julho, não coincide com o ano civil: o PRODES 2025
cobre de agosto de 2024 a julho de 2025.

A cobertura do solo vem da **Coleção 4** do MapBiomas, a única disponível a
10 metros. A versão de 30 m usava a Coleção 11 — a legenda de códigos é a mesma,
mas são produtos diferentes e a classe de um pixel pode divergir entre elas.

---

Análise do projeto NORAD. Dados: PRODES/INPE (camadas anuais de 2026), SICAR, SIGEF e SNCI/INCRA,
MapBiomas Coleção 4, CNUC, FUNAI, IBGE.
