
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

pasta = Path("data/processed")
entrada = pasta / "votos_governador_por_ra.csv"

excluir = {"95", "96"}

votos = defaultdict(lambda: defaultdict(int))
nomes = {}

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")

    for linha in leitor:
        numero = linha["NR_VOTAVEL"].strip()

        if numero in excluir:
            continue

        ra = linha["RA"].strip()
        quantidade = int(linha["QT_VOTOS"])

        votos[ra][numero] += quantidade
        nomes[numero] = linha["NM_VOTAVEL"].strip()

totais = {
    ra: sum(candidatos.values())
    for ra, candidatos in votos.items()
}

regioes = sorted(
    votos,
    key=lambda ra: totais[ra],
    reverse=True
)

totais_candidatos = defaultdict(int)

for candidatos in votos.values():
    for numero, quantidade in candidatos.items():
        totais_candidatos[numero] += quantidade

principais = sorted(
    totais_candidatos,
    key=totais_candidatos.get,
    reverse=True
)[:4]

outros = [
    numero for numero in totais_candidatos
    if numero not in principais
]

fig, ax = plt.subplots(figsize=(14, 12))

base = [0.0] * len(regioes)

for numero in principais + ["OUTROS"]:
    percentuais = []

    for ra in regioes:
        total = totais[ra]

        if numero == "OUTROS":
            quantidade = sum(
                votos[ra].get(n, 0) for n in outros
            )
        else:
            quantidade = votos[ra].get(numero, 0)

        percentual = (
            quantidade / total * 100
            if total > 0 else 0
        )
        percentuais.append(percentual)

    rotulo = (
        "Outros candidatos"
        if numero == "OUTROS"
        else f"{numero} - {nomes[numero]}"
    )

    ax.barh(
        regioes,
        percentuais,
        left=base,
        label=rotulo
    )

    base = [
        anterior + atual
        for anterior, atual in zip(base, percentuais)
    ]

ax.set_xlim(0, 100)
ax.set_xlabel("Percentual dos votos válidos (%)")
ax.set_ylabel("Região Administrativa")
ax.set_title(
    "Distribuição percentual dos votos válidos "
    "por RA - Governador, 1º turno"
)

ax.invert_yaxis()
ax.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.08),
    ncol=2,
    fontsize=9
)

plt.subplots_adjust(bottom=0.18)

plt.tight_layout()

saida = pasta / "percentual_votos_por_ra.png"
plt.savefig(saida, dpi=160, bbox_inches="tight")
plt.show()

print("GRAFICO PERCENTUAL CONCLUIDO")
print("-" * 40)
print(f"Regioes analisadas: {len(regioes)}")
print(f"Candidatos identificados: {len(nomes)}")
print(f"Total de votos validos: {sum(totais.values())}")
print(f"Arquivo: {saida}")
