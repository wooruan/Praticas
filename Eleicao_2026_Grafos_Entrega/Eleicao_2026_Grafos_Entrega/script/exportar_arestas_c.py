
import csv
from pathlib import Path

pasta = Path("data/processed")
entrada = pasta / "grafo_similaridade.gexf"
saida = pasta / "arestas_c.txt"
saida_nomes = pasta / "vertices_c.txt"

import networkx as nx

grafo = nx.read_gexf(entrada)

vertices = sorted(grafo.nodes())
indices = {nome: i for i, nome in enumerate(vertices)}

with open(saida_nomes, "w", encoding="utf-8") as f:
    for i, nome in enumerate(vertices):
        f.write(f"{i};{nome}\n")

with open(saida, "w", encoding="utf-8") as f:
    f.write(f"{len(vertices)} {grafo.number_of_edges()}\n")

    for origem, destino in grafo.edges():
        f.write(f"{indices[origem]} {indices[destino]}\n")

print("EXPORTACAO CONCLUIDA")
print("-" * 40)
print(f"Vertices: {len(vertices)}")
print(f"Arestas: {grafo.number_of_edges()}")
print(f"Arquivo de arestas: {saida}")
print(f"Arquivo de nomes: {saida_nomes}")
