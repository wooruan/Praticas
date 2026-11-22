
import csv
from collections import defaultdict
from pathlib import Path

import networkx as nx

pasta = Path("data/processed")
entrada = pasta / "similaridade_entre_ras.csv"
saida = pasta / "comparacao_limiares.csv"

limiares = [0.990, 0.995, 0.998, 0.999]

comparacoes = []
regioes = set()

with open(entrada, encoding="utf-8-sig", newline="") as f:
    leitor = csv.DictReader(f, delimiter=";")

    for linha in leitor:
        ra1 = linha["RA_1"]
        ra2 = linha["RA_2"]
        similaridade = float(
            linha["SIMILARIDADE"].replace(",", ".")
        )

        regioes.update([ra1, ra2])
        comparacoes.append((ra1, ra2, similaridade))

resultados = []

print("COMPARACAO DE LIMIARES")
print("-" * 65)

for limiar in limiares:
    G = nx.Graph()
    G.add_nodes_from(regioes)

    for ra1, ra2, similaridade in comparacoes:
        if similaridade >= limiar:
            G.add_edge(
                ra1,
                ra2,
                peso=similaridade
            )

    componentes = nx.number_connected_components(G)
    isolados = nx.number_of_isolates(G)

    if G.number_of_edges() > 0:
        comunidades = list(
            nx.community.greedy_modularity_communities(
                G,
                weight="peso"
            )
        )

        modularidade = nx.community.modularity(
            G,
            comunidades,
            weight="peso"
        )
    else:
        comunidades = [{ra} for ra in G.nodes()]
        modularidade = 0.0

    resultado = {
        "LIMIAR": limiar,
        "NOS": G.number_of_nodes(),
        "ARESTAS": G.number_of_edges(),
        "DENSIDADE": round(nx.density(G), 4),
        "COMPONENTES": componentes,
        "ISOLADOS": isolados,
        "COMUNIDADES": len(comunidades),
        "MODULARIDADE": round(modularidade, 4)
    }

    resultados.append(resultado)

    print(
        f"Limiar: {limiar:.3f} | "
        f"Arestas: {G.number_of_edges():3d} | "
        f"Densidade: {nx.density(G):.4f} | "
        f"Comunidades: {len(comunidades):2d} | "
        f"Modularidade: {modularidade:.4f} | "
        f"Isolados: {isolados}"
    )

with open(saida, "w", encoding="utf-8-sig", newline="") as f:
    escritor = csv.DictWriter(
        f,
        fieldnames=resultados[0].keys(),
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(resultados)

print("-" * 65)
print(f"Relatorio: {saida}")
