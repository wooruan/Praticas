
import csv
import re
import unicodedata
from pathlib import Path

entrada = Path("data/processed/todos_locais_pendentes.csv")
saida = Path("data/processed/locais_outros.csv")

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.upper())
    return "".join(
        c for c in texto
        if not unicodedata.combining(c)
    )

padroes = [
    r"\bQNM\s*\d+",
    r"\bQNO\s*\d+",
    r"\bQNQ\s*\d+",
    r"\bQNP\s*\d+",
    r"\bQR\s*\d+",
    r"\bQN\s*\d+",
    r"\bQS\s*\d+",
    r"\bQ\.?\s*\d+",
    r"\bAR\s*\d+",
    r"\bSETOR\b",
    r"\bNUCLEO RURAL\b",
    r"\b(?:BR|DF)[\s-]*\d+"
]

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    linhas = list(csv.DictReader(arquivo, delimiter=";"))

outros = []

for linha in linhas:
    endereco = normalizar(
        linha["DS_LOCAL_VOTACAO_ENDERECO"]
    )

    if not any(re.search(p, endereco) for p in padroes):
        outros.append(linha)

outros.sort(
    key=lambda linha: (
        int(linha["NR_ZONA"]),
        int(linha["NR_LOCAL_VOTACAO"])
    )
)

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")
    escritor.writerow([
        "NR_ZONA",
        "NR_LOCAL_VOTACAO",
        "NM_LOCAL_VOTACAO",
        "DS_LOCAL_VOTACAO_ENDERECO"
    ])

    for linha in outros:
        escritor.writerow([
            linha["NR_ZONA"],
            linha["NR_LOCAL_VOTACAO"],
            linha["NM_LOCAL_VOTACAO"],
            linha["DS_LOCAL_VOTACAO_ENDERECO"]
        ])

print("RELATORIO DE OUTROS CONCLUIDO!")
print(f"Total de locais OUTROS: {len(outros)}")
print(f"Arquivo gerado: {saida}")

