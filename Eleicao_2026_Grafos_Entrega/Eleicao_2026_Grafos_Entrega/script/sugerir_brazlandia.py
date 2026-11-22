
import csv
import unicodedata
from pathlib import Path

entrada = Path("data/processed/revisao_ra_sobradinho_industria.csv")
saida = Path("data/processed/revisao_ra_brazlandia.csv")

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.upper())
    return "".join(
        letra for letra in texto
        if not unicodedata.combining(letra)
    )

padroes = [
    "SETOR NORTE",
    "SETOR TRADICIONAL",
    "SETOR VEREDAS",
    "VILA SAO JOSE"
]

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

    endereco = normalizar(
        linha["DS_LOCAL_VOTACAO_ENDERECO"]
    )

    if any(padrao in endereco for padrao in padroes):
        linha["RA_PROVAVEL"] = "Brazlândia"
        linha["REGRA_UTILIZADA"] = "PADRAO_BRAZLANDIA_REVISAR"
        sugestoes += 1

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("ANALISE DE BRAZLANDIA CONCLUIDA!")
print(f"Novas sugestoes: {sugestoes}")
print(f"Arquivo gerado: {saida}")
