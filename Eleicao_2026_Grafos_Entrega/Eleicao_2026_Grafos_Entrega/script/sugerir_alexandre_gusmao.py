
import csv
import re
import unicodedata
from pathlib import Path

entrada = Path("data/processed/revisao_ra_ceilandia_sol_nascente.csv")
saida = Path("data/processed/revisao_ra_alexandre_gusmao.csv")

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.upper())
    return "".join(
        caractere for caractere in texto
        if not unicodedata.combining(caractere)
    )

padrao = re.compile(
    r"\bINCRA\s*0?[6789]\b|"
    r"\bALEX(?:ANDRE)?\.?\s*GUSMAO\b"
)

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

sugestoes = 0

for linha in linhas:
    if linha["NR_ZONA"] != "16":
        continue

    if linha["STATUS"] != "PENDENTE":
        continue

    if linha["RA_PROVAVEL"].strip():
        continue

    texto = normalizar(
        linha["NM_LOCAL_VOTACAO"] + " " +
        linha["DS_LOCAL_VOTACAO_ENDERECO"]
    )

    if padrao.search(texto):
        linha["RA_PROVAVEL"] = "Brazlândia"
        linha["REGRA_UTILIZADA"] = "INCRA_ALEXANDRE_GUSMAO_REVISAR"
        sugestoes += 1

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("ANALISE DE ALEXANDRE GUSMAO CONCLUIDA!")
print(f"Novas sugestoes: {sugestoes}")
print(f"Arquivo gerado: {saida}")
