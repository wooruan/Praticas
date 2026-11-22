
import csv
import re
import unicodedata
from collections import Counter
from pathlib import Path

entrada = Path("data/processed/revisao_ra_lote_geral.csv")
saida = Path("data/processed/revisao_ra_lote_2.csv")
relatorio = Path("data/processed/auditoria_lote_2.csv")

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.upper())
    return "".join(
        c for c in texto
        if not unicodedata.combining(c)
    )

regras = [
    ("13", r"\b(?:QS|QN|QR)\s*\d+", "Samambaia"),

    ("19", r"\b(?:QNH|EQNG|CND|CNB|EQNH)\s*\d+",
     "Taguatinga"),

    ("9", r"\bEQ\s*\d+\s*/\s*\d+", "Guará"),

    ("11", r"\b(?:EQSW|SQSW|SHCSW)\b|SETOR SUDOESTE",
     "Sudoeste/Octogonal"),

    ("15", r"\bRUA\s+\d+\s+(?:SUL|NORTE)\b",
     "Águas Claras"),

    ("15", r"\bAVENIDA SIBIPIRUNA\b|\bRUA MANACA\b",
     "Águas Claras"),

    ("18", r"\bJARDIM MANGUEIRAL\b", "Jardim Botânico"),

    ("3", r"\bEQNJ\s*\d+", "Ceilândia"),

    ("14", r"\bHCGN\s*\d+|CAMPUS UNIVERSITARIO DARCY RIBEIRO",
     "Plano Piloto"),

    ("2", r"\bGRANJA DO TORTO\b", "Lago Norte"),

    ("4", r"\bPORTO RICO\b", "Santa Maria"),
]

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

contagem = Counter()
auditoria = []

for linha in linhas:
    if linha["STATUS"] != "PENDENTE":
        continue

    if linha["RA_PROVAVEL"].strip():
        continue

    zona = linha["NR_ZONA"]

    texto = normalizar(
        linha["NM_LOCAL_VOTACAO"] + " " +
        linha["DS_LOCAL_VOTACAO_ENDERECO"]
    )

    correspondencias = set()

    for zona_regra, expressao, ra in regras:
        if zona == zona_regra and re.search(expressao, texto):
            correspondencias.add(ra)

    if len(correspondencias) == 1:
        ra = correspondencias.pop()

        linha["RA_PROVAVEL"] = ra
        linha["REGRA_UTILIZADA"] = "LOTE_2_REVISAR"

        contagem[ra] += 1

        auditoria.append({
            "NR_ZONA": zona,
            "NR_LOCAL_VOTACAO": linha["NR_LOCAL_VOTACAO"],
            "NM_LOCAL_VOTACAO": linha["NM_LOCAL_VOTACAO"],
            "DS_LOCAL_VOTACAO_ENDERECO":
                linha["DS_LOCAL_VOTACAO_ENDERECO"],
            "RA_SUGERIDA": ra
        })

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

with open(relatorio, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=[
            "NR_ZONA",
            "NR_LOCAL_VOTACAO",
            "NM_LOCAL_VOTACAO",
            "DS_LOCAL_VOTACAO_ENDERECO",
            "RA_SUGERIDA"
        ],
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(auditoria)

print("\nSEGUNDA CLASSIFICACAO EM LOTE CONCLUIDA!")
print("-" * 45)

for ra, quantidade in contagem.most_common():
    print(f"{ra}: {quantidade}")

print("-" * 45)
print(f"Novas sugestoes: {len(auditoria)}")
print(f"Total de locais: {len(linhas)}")

restantes = sum(
    1 for linha in linhas
    if linha["STATUS"] == "PENDENTE"
    and not linha["RA_PROVAVEL"].strip()
)

print(f"Locais ainda sem sugestao: {restantes}")
print(f"Arquivo gerado: {saida}")
print(f"Auditoria gerada: {relatorio}")
