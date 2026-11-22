
import csv
import unicodedata
from pathlib import Path

entrada = Path("data/processed/revisao_ra_corrigida.csv")
saida = Path("data/processed/revisao_ra_arapoanga.csv")

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.upper())
    return "".join(
        letra for letra in texto
        if not unicodedata.combining(letra)
    )

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

sugestoes = 0

for linha in linhas:
    if linha["STATUS"] != "PENDENTE":
        continue

    if linha["RA_PROVAVEL"].strip():
        continue

    texto = normalizar(
        linha["NM_LOCAL_VOTACAO"] + " " +
        linha["DS_LOCAL_VOTACAO_ENDERECO"]
    )

    if "ARAPOANGA" in texto:
        linha["RA_PROVAVEL"] = "Arapoanga"
        linha["REGRA_UTILIZADA"] = "REFERENCIA_EXPLICITA_REVISAR"
        sugestoes += 1

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("ANALISE DE ARAPOANGA CONCLUIDA!")
print(f"Novas sugestoes: {sugestoes}")
print(f"Arquivo gerado: {saida}")
