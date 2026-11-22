
import csv
from pathlib import Path

entrada = Path("data/processed/revisao_ra_sobradinho.csv")
saida = Path("data/processed/revisao_ra_sobradinho_industria.csv")

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

sugestoes = 0

for linha in linhas:
    if (
        linha["NR_ZONA"] == "5"
        and linha["NR_LOCAL_VOTACAO"] == "1767"
        and linha["STATUS"] == "PENDENTE"
        and not linha["RA_PROVAVEL"].strip()
        and "ST.DE IND. DE SOB." in
        linha["DS_LOCAL_VOTACAO_ENDERECO"].upper()
    ):
        linha["RA_PROVAVEL"] = "Sobradinho"
        linha["REGRA_UTILIZADA"] = "SETOR_INDUSTRIA_SOBRADINHO_REVISAR"
        sugestoes += 1

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("ANALISE DO SETOR DE INDUSTRIA CONCLUIDA!")
print(f"Novas sugestoes: {sugestoes}")
print(f"Arquivo gerado: {saida}")
