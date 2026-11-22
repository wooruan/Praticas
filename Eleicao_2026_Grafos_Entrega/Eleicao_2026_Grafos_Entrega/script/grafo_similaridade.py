
import csv
import math
from collections import defaultdict
from pathlib import Path

import networkx as nx
import matplotlib.pyplot as plt

pasta = Path("data/processed")
entrada = pasta / "votos_governador_por_ra.csv"

saida_grafo = pasta / "grafo_similaridade.gexf"
saida_imagem = pasta / "grafo_similaridade.png"
saida_relatorio = pasta / "similaridade_entre_ras.csv"

LIMIAR = 0.998
MIN_VOTOS = 1000

EXCLUIR = {"95", "96"}

votos = defaultdict(lambda: defaultdict(int))
candidatos = set()

with open(entrada, encoding="utf-8-sig", newline="") as f:
    leitor = csv.DictReader(f, delimiter=";")

    for linha in leitor:
        numero = linha["NR_VOTAVEL"].strip()

        if numero in EXCLUIR:
            continue

        ra = linha["RA"].strip()
        quantidade = int(linha["QT_VOTOS"])

        votos[ra][numero] += quantidade
        candidatos.add(numero)

candidatos = sorted(candidatos, key=int)

totais = {
    ra: sum(valores.values())
    for ra, valores in votos.items()
}

regioes = sorted(
    ra for ra in votos
    if totais[ra] >= MIN_VOTOS
)

vetores = {}

for ra in regioes:
    vetores[ra] = [
        votos[ra].get(numero, 0) / totais[ra]
        for numero in candidatos
    ]

def similaridade_cosseno(a, b):
    produto = sum(x * y for x, y in zip(a, b))

    norma_a = math.sqrt(sum(x*x for x in a))
    norma_b = math.sqrt(sum(y*y for y in b))

    if norma_a == 0 or norma_b == 0:
        return 0.0

    return produto / (norma_a * norma_b)

G = nx.Graph()

for ra in regioes:
    G.add_node(
        ra,
        votos_validos=totais[ra]
    )

comparacoes = []

for i, ra1 in enumerate(regioes):
    for ra2 in regioes[i+1:]:
        similaridade = similaridade_cosseno(
            vetores[ra1],
            vetores[ra2]
        )

        comparacoes.append(
            (ra1, ra2, similaridade)
        )

        if similaridade >= LIMIAR:
            G.add_edge(
                ra1,
                ra2,
                peso=similaridade
            )

with open(
    saida_relatorio,
    "w",
    encoding="utf-8-sig",
    newline=""
) as f:
    escritor = csv.writer(f, delimiter=";")

    escritor.writerow([
        "RA_1",
        "RA_2",
        "SIMILARIDADE"
    ])

    for ra1, ra2, sim in sorted(
        comparacoes,
        key=lambda x: x[2],
        reverse=True
    ):
        escritor.writerow([
            ra1,
            ra2,
            f"{sim:.6f}"
        ])

nx.write_gexf(G, saida_grafo)

plt.figure(figsize=(15, 11))

posicoes = nx.spring_layout(
    G,
    seed=42,
    weight="peso"
)

tamanhos = [
    300 + 100 * math.log10(totais[ra])
    for ra in G.nodes()
]

nx.draw_networkx_nodes(
    G,
    posicoes,
    node_size=tamanhos,
    alpha=0.85
)

nx.draw_networkx_edges(
    G,
    posicoes,
    alpha=0.25,
    width=1.2
)

nx.draw_networkx_labels(
    G,
    posicoes,
    font_size=8
)

plt.title(
    "Grafo de similaridade eleitoral entre RAs\n"
    f"Cosseno >= {LIMIAR} | "
    f"Mínimo de {MIN_VOTOS} votos válidos"
)

plt.axis("off")
plt.tight_layout()
plt.savefig(
    saida_imagem,
    dpi=180,
    bbox_inches="tight"
)
plt.show()

componentes = list(nx.connected_components(G))

print("GRAFO DE SIMILARIDADE CONCLUIDO")
print("-" * 45)
print(f"RAs na base: {len(votos)}")
print(f"RAs analisadas: {len(regioes)}")
print(f"RAs excluidas por poucos votos: {len(votos) - len(regioes)}")
print(f"Comparacoes realizadas: {len(comparacoes)}")
print(f"Nos: {G.number_of_nodes()}")
print(f"Arestas: {G.number_of_edges()}")
print(f"Componentes conectados: {len(componentes)}")
print(f"Grafo: {saida_grafo}")
print(f"Imagem: {saida_imagem}")
print(f"Relatorio: {saida_relatorio}")

print("\nREGIOES EXCLUIDAS")
print("-" * 45)

for ra in sorted(votos):
    if totais[ra] < MIN_VOTOS:
        print(f"{ra}: {totais[ra]} votos validos")

print("\nREGIOES ISOLADAS")
print("-" * 45)

for ra in sorted(nx.isolates(G)):
    print(f"{ra}: {totais[ra]} votos validos")
