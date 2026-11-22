
import networkx as nx
from pathlib import Path

pasta = Path("data/processed")
arquivo = pasta / "grafo_similaridade.gexf"

G = nx.read_gexf(arquivo)

print("ANALISE DO GRAFO ELEITORAL")
print("-" * 45)

print(f"Nos: {G.number_of_nodes()}")
print(f"Arestas: {G.number_of_edges()}")
print(f"Densidade: {nx.density(G):.4f}")

componentes = sorted(
    nx.connected_components(G),
    key=len,
    reverse=True
)

print(f"Componentes conectados: {len(componentes)}")
print(f"Maior componente: {len(componentes[0]) if componentes else 0}")

print("\nGRAU DE CADA RA")
print("-" * 45)

graus = sorted(
    G.degree(),
    key=lambda item: item[1],
    reverse=True
)

for ra, grau in graus:
    print(f"{ra:<30} {grau:>3}")

print("\nCOMUNIDADES DETECTADAS")
print("-" * 45)

if G.number_of_edges() > 0:
    comunidades = nx.community.greedy_modularity_communities(
        G,
        weight="peso"
    )
else:
    comunidades = [
        {no} for no in G.nodes()
    ]

for numero, comunidade in enumerate(comunidades, 1):
    print(f"\nComunidade {numero} ({len(comunidade)} RAs)")

    for ra in sorted(comunidade):
        print(f"  - {ra}")

import matplotlib.pyplot as plt

cores_disponiveis = [
    "#3B82F6",
    "#16A085",
    "#A477C8"
]

mapa_cores = {}

for indice, comunidade in enumerate(comunidades):
    cor = cores_disponiveis[indice % len(cores_disponiveis)]

    for ra in comunidade:
        mapa_cores[ra] = cor

cores_nos = [
    mapa_cores[ra]
    for ra in G.nodes()
]

posicoes = nx.spring_layout(
    G,
    seed=42,
    k=1.5,
    iterations=200
)

plt.figure(figsize=(18, 13))

nx.draw_networkx_edges(
    G,
    posicoes,
    alpha=0.12,
    width=0.8
)

nx.draw_networkx_nodes(
    G,
    posicoes,
    node_color=cores_nos,
    node_size=850,
    alpha=0.9
)

nx.draw_networkx_labels(
    G,
    posicoes,
    font_size=8
)

plt.title(
    "Comunidades de similaridade eleitoral entre RAs",
    fontsize=16
)

plt.axis("off")
plt.tight_layout()

saida = pasta / "comunidades_eleitorais.png"

plt.savefig(
    saida,
    dpi=180,
    bbox_inches="tight"
)

plt.show()

print(f"\nImagem das comunidades: {saida}")
modularidade = nx.community.modularity(
    G,
    comunidades,
    weight="peso"
)

print("\nQUALIDADE DAS COMUNIDADES")
print("-" * 45)
print(f"Modularidade: {modularidade:.4f}")
print(f"Comunidades: {len(comunidades)}")
