
import csv
from pathlib import Path

entrada = Path("data/processed/revisao_ra_lote_3.csv")
saida = Path("data/processed/ultimos_50.csv")

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)

pendentes = [
    linha for linha in linhas
    if not linha["RA_PROVAVEL"].strip()
    and not linha["RA"].strip()
]

pendentes.sort(
    key=lambda x: (
        int(x["NR_ZONA"]),
        int(x["NR_LOCAL_VOTACAO"])
    )
)

colunas = [
    "NR_ZONA",
    "NR_LOCAL_VOTACAO",
    "NM_LOCAL_VOTACAO",
    "DS_LOCAL_VOTACAO_ENDERECO"
]

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()

    for linha in pendentes:
        escritor.writerow({
            coluna: linha[coluna] for coluna in colunas
        })

print("ULTIMOS PENDENTES")
print("-" * 40)
print(f"Quantidade: {len(pendentes)}")
print(f"Arquivo: {saida}")
