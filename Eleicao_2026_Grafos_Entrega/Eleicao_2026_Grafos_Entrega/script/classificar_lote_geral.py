
import csv
import re
import unicodedata
from collections import Counter
from pathlib import Path

entrada = Path("data/processed/revisao_ra_uibra.csv")
saida = Path("data/processed/revisao_ra_lote_geral.csv")

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.upper())
    return "".join(
        c for c in texto
        if not unicodedata.combining(c)
    )

regras = [
    ("2", r"\bVARJAO\b", "Varjão"),
    ("2", r"\bITAPOA\b", "Itapoã"),
    ("2", r"\bPARANOA\b", "Paranoá"),

    ("4", r"\bSANTA MARIA\b|\bCL\s*\d{3}\b",
     "Santa Maria"),

    ("9", r"\bVILA ESTRUTURAL\b", "SCIA/Estrutural"),
    ("9", r"\bGUARA\s*II\b", "Guará"),

    ("10", r"\bCANDANGOLANDIA\b", "Candangolândia"),
    ("10", r"\bNUCLEO BANDEIRANTE\b", "Núcleo Bandeirante"),

    ("11", r"\bOCTOGONAL\b", "Sudoeste/Octogonal"),

    ("15", r"\bAVENIDA (?:ARAU CARIAS|ARAUCARIAS|CASTANHEIRAS|JEQUITIBA)\b",
     "Águas Claras"),

    ("19", r"\bVICENTE PIRES\b", "Vicente Pires"),

    ("20", r"\bPOR DO SOL\b", "Sol Nascente/Pôr do Sol"),
]

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

contagem = Counter()
alterados = []

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
        linha["REGRA_UTILIZADA"] = "LOTE_GERAL_REVISAR"

        contagem[ra] += 1
        alterados.append((
            zona,
            linha["NR_LOCAL_VOTACAO"],
            ra
        ))

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("\nCLASSIFICACAO EM LOTE CONCLUIDA!")
print("-" * 45)

for ra, quantidade in contagem.most_common():
    print(f"{ra}: {quantidade}")

print("-" * 45)
print(f"Novas sugestoes: {len(alterados)}")
print(f"Total de locais: {len(linhas)}")
print(f"Arquivo gerado: {saida}")

print("\nLOCAIS ALTERADOS:")
for zona, local, ra in alterados:
    print(f"Zona {zona} | Local {local} | {ra}")
