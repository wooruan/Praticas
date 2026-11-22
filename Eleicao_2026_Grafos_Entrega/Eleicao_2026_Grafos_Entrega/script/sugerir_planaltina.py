
import csv
import re
import unicodedata
from pathlib import Path

entrada = Path("data/processed/revisao_ra_arapoanga.csv")
saida = Path("data/processed/revisao_ra_planaltina.csv")

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.upper())
    return "".join(
        letra for letra in texto
        if not unicodedata.combining(letra)
    )

padrao = re.compile(
    r"\bSRL\b|\bSRN\b|\bBURITIS\b|\bSETOR EDUCACIONAL\b"
)

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

sugestoes = 0

for linha in linhas:
    if linha["NR_ZONA"] != "6":
        continue

    if linha["STATUS"] != "PENDENTE":
        continue

    if linha["RA_PROVAVEL"].strip():
        continue

    endereco = normalizar(
        linha["DS_LOCAL_VOTACAO_ENDERECO"]
    )

    if padrao.search(endereco):
        linha["RA_PROVAVEL"] = "Planaltina"
        linha["REGRA_UTILIZADA"] = "PADRAO_ENDERECO_REVISAR"
        sugestoes += 1

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("ANALISE DE PLANALTINA CONCLUIDA!")
print(f"Novas sugestoes: {sugestoes}")
print(f"Arquivo gerado: {saida}")
