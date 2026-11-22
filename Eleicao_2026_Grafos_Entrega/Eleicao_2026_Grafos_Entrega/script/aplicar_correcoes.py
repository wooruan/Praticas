
import csv
from pathlib import Path

entrada = Path("data/processed/locais_votacao_df.csv")
correcoes = Path("data/correcoes_ra.csv")
saida = Path("data/processed/locais_com_ra_df.csv")

mapa = {}

with open(correcoes, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")

    for linha in leitor:
        chave = (
            linha["NR_ZONA"],
            linha["NR_LOCAL_VOTACAO"]
        )
        mapa[chave] = linha["RA"]

total_corrigidos = 0

with open(entrada, encoding="utf-8-sig", newline="") as origem:
    leitor = csv.DictReader(origem, delimiter=";")
    colunas = leitor.fieldnames

    with open(saida, "w", encoding="utf-8-sig", newline="") as destino:
        escritor = csv.DictWriter(
            destino,
            fieldnames=colunas,
            delimiter=";"
        )
        escritor.writeheader()

        for linha in leitor:
            chave = (
                linha["NR_ZONA"],
                linha["NR_LOCAL_VOTACAO"]
            )

            if chave in mapa:
                linha["RA"] = mapa[chave]
                total_corrigidos += 1

            escritor.writerow(linha)

print("CORRECOES APLICADAS!")
print(f"Locais corrigidos: {total_corrigidos}")
print(f"Arquivo gerado: {saida}")
