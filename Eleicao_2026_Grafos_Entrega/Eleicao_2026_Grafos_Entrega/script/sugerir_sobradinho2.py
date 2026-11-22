
import csv
import re
from pathlib import Path

entrada = Path("data/processed/revisao_ra_localidades.csv")
saida = Path("data/processed/revisao_ra_sobradinho2.csv")

padrao = re.compile(r"\bAR\s*\d{1,2}\b", re.IGNORECASE)

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

sugestoes = 0

for linha in linhas:
    if linha["NR_ZONA"] != "5":
        continue

    if linha["STATUS"] != "PENDENTE":
        continue

    if linha["RA_PROVAVEL"].strip():
        continue

    endereco = linha["DS_LOCAL_VOTACAO_ENDERECO"]

    if padrao.search(endereco):
        linha["RA_PROVAVEL"] = "Sobradinho II"
        linha["REGRA_UTILIZADA"] = "PADRAO_AR_SOBRADINHO_II_REVISAR"
        sugestoes += 1

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("ANALISE DE SOBRADINHO II CONCLUIDA!")
print(f"Novas sugestoes: {sugestoes}")
print(f"Arquivo gerado: {saida}")
