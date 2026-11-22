import csv
from collections import Counter

arquivo = "data/raw/votacao_secao_2026_DF/votacao_secao_2026_DF.csv"

cargos = Counter()

with open(arquivo, "r", encoding="latin-1", newline="") as csvfile:
    leitor = csv.DictReader(csvfile, delimiter=";")

    for linha in leitor:
        cargo = linha["DS_CARGO"]
        cargos[cargo] += 1

print("CARGOS ENCONTRADOS NO CSV:")

for cargo, quantidade in cargos.items():
    print(f"{cargo}: {quantidade} registros")
