
import csv
import unicodedata
from pathlib import Path

entrada = Path("data/processed/locais_com_ra_df.csv")
saida = Path("data/processed/locais_ra_sugeridas.csv")

regras = {
    "RIACHO FUNDO II": "Riacho Fundo II",
    "RIACHO FUNDO": "Riacho Fundo",
    "SAO SEBASTIAO": "São Sebastião",
    "JARDIM BOTANICO": "Jardim Botânico",
    "AGUAS CLARAS": "Águas Claras",
    "RECANTO DAS EMAS": "Recanto das Emas",
    "CEILANDIA": "Ceilândia",
    "TAGUATINGA": "Taguatinga",
    "LAGO SUL": "Lago Sul",
    "LAGO NORTE": "Lago Norte",
    "SOBRADINHO II": "Sobradinho II",
    "SOBRADINHO": "Sobradinho",
    "SAMAMBAIA": "Samambaia",
    "PLANALTINA": "Planaltina",
    "GAMA": "Gama"
}

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.upper())
    return "".join(
        letra for letra in texto
        if not unicodedata.combining(letra)
    )

total_sugestoes = 0
pendentes = 0

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)

for linha in linhas:
    if linha["RA"].strip():
        linha["STATUS"] = "CORRECAO_ANTERIOR"
        continue

    texto = normalizar(
        linha["NM_LOCAL_VOTACAO"] + " " +
        linha["DS_LOCAL_VOTACAO_ENDERECO"]
    )

    correspondencias = set()

    for palavra, ra in regras.items():
        if palavra in texto:
            correspondencias.add(ra)

    if "Riacho Fundo II" in correspondencias:
        correspondencias.discard("Riacho Fundo")

    if "Sobradinho II" in correspondencias:
        correspondencias.discard("Sobradinho")

    if len(correspondencias) == 1:
        linha["RA"] = correspondencias.pop()
        linha["STATUS"] = "SUGERIDA"
        total_sugestoes += 1
    else:
        linha["STATUS"] = "PENDENTE"
        pendentes += 1

colunas = list(linhas[0].keys())

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("IDENTIFICACAO CONCLUIDA!")
print(f"RAs sugeridas: {total_sugestoes}")
print(f"Locais pendentes: {pendentes}")
print(f"Arquivo gerado: {saida}")
