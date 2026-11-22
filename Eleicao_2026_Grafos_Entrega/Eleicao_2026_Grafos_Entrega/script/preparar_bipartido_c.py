
import csv
from collections import defaultdict
from pathlib import Path

pasta = Path("data/processed")

entrada = pasta / "votos_governador_por_ra.csv"
saida = pasta / "votacao_governador_df_2026.csv"

votos = defaultdict(int)
totais_ra = defaultdict(int)

with open(entrada, encoding="utf-8-sig", newline="") as f:
    leitor = csv.DictReader(f, delimiter=";")

    for linha in leitor:
        numero = linha["NR_VOTAVEL"].strip()

        if numero in {"95", "96"}:
            continue

        ra = linha["RA"].strip()
        candidato = linha["NM_VOTAVEL"].strip()
        quantidade = int(linha["QT_VOTOS"])

        votos[(ra, candidato)] += quantidade
        totais_ra[ra] += quantidade

with open(saida, "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f, delimiter=";")

    escritor.writerow(["RA", "CANDIDATO", "PERCENTUAL"])

    for (ra, candidato), quantidade in sorted(votos.items()):
        if totais_ra[ra] == 0:
            continue

        percentual = 100.0 * quantidade / totais_ra[ra]

        escritor.writerow([
            ra,
            candidato,
            f"{percentual:.6f}"
        ])

print("CSV DO GRAFO BIPARTIDO PREPARADO")
print("----------------------------------------")
print(f"Regioes Administrativas: {len(totais_ra)}")
print(f"Candidatos: {len(set(c for _, c in votos))}")
print(f"Conexoes: {len(votos)}")
print(f"Arquivo: {saida}")
