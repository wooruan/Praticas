
import csv
from pathlib import Path

entrada = Path("data/processed/revisao_ra_alexandre_gusmao.csv")
saida = Path("data/processed/revisao_ra_uibra.csv")

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

sugestoes = 0

for linha in linhas:
    if (
        linha["NR_ZONA"] == "16"
        and linha["NR_LOCAL_VOTACAO"] == "1627"
        and linha["STATUS"] == "PENDENTE"
        and not linha["RA_PROVAVEL"].strip()
        and "BRAZLÂNDIA" in linha["NM_LOCAL_VOTACAO"].upper()
    ):
        linha["RA_PROVAVEL"] = "Brazlândia"
        linha["REGRA_UTILIZADA"] = "UIBRA_NOME_EXPLICITO_REVISAR"
        sugestoes += 1

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("ANALISE DA UIBRA CONCLUIDA!")
print(f"Novas sugestoes: {sugestoes}")
print(f"Arquivo gerado: {saida}")

