
import csv
import re
from pathlib import Path

entrada = Path("data/processed/revisao_ra_brazlandia.csv")
saida = Path("data/processed/revisao_ra_ceilandia_sol_nascente.csv")

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

sugestoes_ceilandia = 0
sugestoes_sol_nascente = 0

for linha in linhas:
    if linha["NR_ZONA"] != "16":
        continue

    if linha["STATUS"] != "PENDENTE":
        continue

    if linha["RA_PROVAVEL"].strip():
        continue

    endereco = linha["DS_LOCAL_VOTACAO_ENDERECO"].upper()

    if "SETOR HABITACIONAL SOL NASCENTE" in endereco:
        linha["RA_PROVAVEL"] = "Sol Nascente/Pôr do Sol"
        linha["REGRA_UTILIZADA"] = "SOL_NASCENTE_EXPLICITO_REVISAR"
        sugestoes_sol_nascente += 1

    elif re.search(r"\bQN[QO]\s*\d+\b", endereco):
        linha["RA_PROVAVEL"] = "Ceilândia"
        linha["REGRA_UTILIZADA"] = "QNQ_QNO_ZONA16_REVISAR"
        sugestoes_ceilandia += 1

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("ANALISE DE CEILANDIA E SOL NASCENTE CONCLUIDA!")
print(f"Sugestoes para Ceilandia: {sugestoes_ceilandia}")
print(f"Sugestoes para Sol Nascente: {sugestoes_sol_nascente}")
print(f"Total de novas sugestoes: {sugestoes_ceilandia + sugestoes_sol_nascente}")
print(f"Arquivo gerado: {saida}")
