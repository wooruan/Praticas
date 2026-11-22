
import csv
import unicodedata
from pathlib import Path

entrada = Path("data/processed/revisao_ra_planaltina.csv")
saida = Path("data/processed/revisao_ra_planaltina_v2.csv")

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.upper())
    return "".join(
        letra for letra in texto
        if not unicodedata.combining(letra)
    )

sugestoes = 0

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

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

    if "SETOR RESIDENCIAL NORTE" in endereco:
        linha["RA_PROVAVEL"] = "Planaltina"
        linha["REGRA_UTILIZADA"] = "SETOR_RESIDENCIAL_NORTE_REVISAR"
        sugestoes += 1

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("COMPLEMENTO DE PLANALTINA CONCLUIDO!")
print(f"Novas sugestoes: {sugestoes}")
print(f"Arquivo gerado: {saida}")
