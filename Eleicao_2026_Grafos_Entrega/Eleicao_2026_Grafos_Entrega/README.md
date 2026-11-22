# Projeto de Grafos — Análise Eleitoral 2026

## Objetivo

Representar e analisar dados eleitorais e relações territoriais por meio de grafos implementados em C, com preparação de dados em Python.

## Organização do projeto

- `main.c`: execução dos módulos.
- `grafo.c` / `grafo.h`: estrutura do grafo com listas de adjacência, inserção de arestas e liberação de memória.
- `analise_df.c` / `analise_df.h`: grafo bipartido de regiões administrativas e candidatos; similaridade entre RAs.
- `analise_nacional.c` / `analise_nacional.h`: contiguidade entre UFs, BFS, análise nacional, DFS e Kruskal.
- `dados_nacionais.h`: definições auxiliares para dados nacionais.
- `script/`: scripts Python para tratamento dos dados.
- `data/nacional/fronteiras_ufs.csv`: fronteiras entre UFs.
- `data/processed/votacao_governador_df_2026.csv`: dados preparados para o DF.
- `data/processed/votacao_presidente_estados_2026.csv`: dados preparados para análise nacional.
- `teste_*.c`: testes isolados (opcionais na entrega).

## Como compilar

No terminal, na pasta raiz do projeto, com GCC instalado:

```bash
gcc -Wall -Wextra -std=c11 main.c grafo.c analise_df.c analise_nacional.c -o eleicoes_2026.exe -lm
```

## Como executar

No PowerShell do Windows:

```powershell
.\eleicoes_2026.exe
```

É necessário executar na pasta raiz para que os caminhos relativos em `data/` sejam encontrados.

Para salvar os resultados em um arquivo:

```powershell
.\eleicoes_2026.exe > resultado_execucao.txt
```

## Resultados observados na execução apresentada

- DF: 34 regiões administrativas, 11 candidatos, 45 vértices e 361 arestas no grafo bipartido.
- Similaridade entre RAs: 111 arestas e 6 componentes no limiar 0,998.
- Territorial: 27 UFs, 50 fronteiras, e BFS alcançando 27 UFs a partir do DF.
- Nacional: 27 UFs, 13 candidatos, 351 arestas.
- Kruskal: 26 arestas selecionadas, peso total informado 0,92.
- DFS: 6 clusters com limiar 0,95 e 13 clusters com limiar 0,97.

## Dados e metodologia

Os arquivos de entrada utilizados pelo programa são CSVs previamente processados. A pasta `script/` contém as rotinas responsáveis pela preparação e pelo tratamento dos dados.

Os dados brutos utilizados durante o desenvolvimento foram mantidos separadamente. Esta versão de entrega contém os arquivos CSV processados necessários para a execução das análises eleitorais.

**Observação:** Os resultados apresentados não devem ser considerados oficiais sem a devida validação das fontes de dados.

## Apresentação

O projeto possui uma apresentação em vídeo disponibilizada no YouTube, explicando a estrutura dos grafos, o tratamento dos dados, os módulos desenvolvidos e os algoritmos BFS, DFS e Kruskal.

**Link do vídeo:** [https://youtu.be/RoO6BMRJhgA]

