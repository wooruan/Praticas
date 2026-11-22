
import csv
from collections import defaultdict
from pathlib import Path

entrada = Path(
    "data/raw/votacao_secao_2026_BR/votacao_secao_2026_BR.csv"
)

saida = Path(
    "data/processed/votacao_presidente_estados_2026.csv"
)

votos = defaultdict(int)
totais_uf = defaultdict(int)

with entrada.open(
    "r",
    encoding="latin-1",
    newline=""
) as arquivo:

    leitor = csv.DictReader(arquivo, delimiter=";")

    for linha in leitor:
        if linha["NR_TURNO"] != "1":
            continue

        if linha["CD_CARGO"] != "1":
            continue

        numero = linha["NR_VOTAVEL"].strip()

        if numero in {"95", "96"}:
            continue

        uf = linha["SG_UF"].strip()

        if uf == "ZZ":
            continue

        candidato = linha["NM_VOTAVEL"].strip()
        quantidade = int(linha["QT_VOTOS"])

        votos[(uf, candidato)] += quantidade
        totais_uf[uf] += quantidade

saida.parent.mkdir(parents=True, exist_ok=True)

with saida.open(
    "w",
    encoding="utf-8",
    newline=""
) as arquivo:

    escritor = csv.writer(arquivo, delimiter=";")

    escritor.writerow([
        "UF",
        "CANDIDATO",
        "VOTOS",
        "PERCENTUAL"
    ])

    for (uf, candidato), quantidade in sorted(votos.items()):
        total = totais_uf[uf]

        if total == 0:
            continue

        percentual = 100 * quantidade / total

        escritor.writerow([
            uf,
            candidato,
            quantidade,
            f"{percentual:.6f}"
        ])

print("\nVOTACAO PRESIDENCIAL AGRUPADA")
print("----------------------------------------")
print(f"UFs: {len(totais_uf)}")
print(f"Candidatos: {len(set(c for _, c in votos))}")
print(f"Registros UF/candidato: {len(votos)}")
print(f"Arquivo: {saida}")
