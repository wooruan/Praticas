
import csv
from collections import defaultdict
from pathlib import Path

import networkx as nx
import matplotlib.pyplot as plt

pasta = Path("data/processed")
entrada = pasta / "votos_governador_por_ra.csv"
saida = pasta / "grafo_eleitoral.gexf"

G = nx.Graph()
totais = defaultdict(int)

with open(entrada, encoding="utf-8-sig", newline="") as f:
    leitor = csv.DictReader(f, delimiter=";")

    for linha in leitor:
        ra = linha["RA"].strip()
        numero = linha["NR_VOTAVEL"].strip()
        nome = linha["NM_VOTAVEL"].strip()
        votos = int(linha["QT_VOTOS"])

        candidato = f"CAND_{numero}"

        G.add_node(
            f"RA_{ra}",
            tipo="RA",
            nome=ra
        )

        G.add_node(
            candidato,
            tipo="CANDIDATO",
            nome=nome
        )

        G.add_edge(
            f"RA_{ra}",
            candidato,
            peso=votos
        )

        totais[ra] += votos

nx.write_gexf(G, saida)

print("GRAFO ELEITORAL CRIADO")
print("-" * 40)
print(f"Nos: {G.number_of_nodes()}")
print(f"Arestas: {G.number_of_edges()}")
print(f"Arquivo: {saida}")

ordenados = sorted(
    totais.items(),
    key=lambda item: item[1],
    reverse=True
)

nomes = [item[0] for item in ordenados]
valores = [item[1] for item in ordenados]

plt.figure(figsize=(12, 10))
plt.barh(nomes[::-1], valores[::-1])
plt.xlabel("Quantidade de votos")
plt.ylabel("Região Administrativa")
plt.title("Votos para governador por RA - 1º turno")
plt.tight_layout()

imagem = pasta / "votos_por_ra.png"
plt.savefig(imagem, dpi=160)
plt.show()

print(f"Grafico: {imagem}")
