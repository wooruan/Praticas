
import csv
from pathlib import Path

entrada = Path("data/processed/revisao_ra.csv")
saida = Path("data/processed/revisao_ra_corrigida.csv")

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

corrigidos = 0

for linha in linhas:
    if (
        linha["NR_ZONA"] == "16"
        and linha["NM_LOCAL_VOTACAO"].strip()
        == "CENTRO DE ENSINO FUNDAMENTAL 28"
        and "SOL NASCENTE" in linha["DS_LOCAL_VOTACAO_ENDERECO"].upper()
    ):
        linha["RA_PROVAVEL"] = "Sol Nascente/Pôr do Sol"
        linha["REGRA_UTILIZADA"] = "ENDERECO_EXPLICITO_REVISAR"
        corrigidos += 1

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("REVISAO CONCLUIDA!")
print(f"Locais ajustados: {corrigidos}")
print(f"Arquivo gerado: {saida}")
