
import csv
import re
import unicodedata
from collections import Counter
from pathlib import Path

entrada = Path("data/processed/todos_locais_pendentes.csv")
saida = Path("data/processed/padroes_gerais.csv")

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.upper())
    return "".join(
        c for c in texto
        if not unicodedata.combining(c)
    )

padroes = {
    "QNM": r"\bQNM\s*\d+",
    "QNO": r"\bQNO\s*\d+",
    "QNQ": r"\bQNQ\s*\d+",
    "QNP": r"\bQNP\s*\d+",
    "QR": r"\bQR\s*\d+",
    "QN": r"\bQN\s*\d+",
    "QS": r"\bQS\s*\d+",
    "Q": r"\bQ\.?\s*\d+",
    "AR": r"\bAR\s*\d+",
    "SETOR": r"\bSETOR\b",
    "NUCLEO_RURAL": r"\bNUCLEO RURAL\b",
    "RODOVIA": r"\b(?:BR|DF)[\s-]*\d+",
    "OUTROS": r".*"
}

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    linhas = list(csv.DictReader(arquivo, delimiter=";"))

contagem = Counter()

for linha in linhas:
    endereco = normalizar(
        linha["DS_LOCAL_VOTACAO_ENDERECO"]
    )

    categoria = "OUTROS"

    for nome, expressao in padroes.items():
        if nome == "OUTROS":
            continue

        if re.search(expressao, endereco):
            categoria = nome
            break

    contagem[(linha["NR_ZONA"], categoria)] += 1

resultado = sorted(
    contagem.items(),
    key=lambda item: (-item[1], int(item[0][0]))
)

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")
    escritor.writerow(["NR_ZONA", "PADRAO", "QUANTIDADE"])

    for (zona, padrao), quantidade in resultado:
        escritor.writerow([zona, padrao, quantidade])

print("\nANALISE DE PADROES CONCLUIDA!")
print("-" * 45)

for (zona, padrao), quantidade in resultado[:30]:
    print(f"Zona {zona:>3} | {padrao:<15} | {quantidade:>3}")

print(f"\nTotal analisado: {len(linhas)}")
print(f"Arquivo gerado: {saida}")
