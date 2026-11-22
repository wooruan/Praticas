
import csv
from pathlib import Path

entrada = Path("data/processed/governador_df_turno1.csv")
saida = Path("data/processed/locais_votacao_df.csv")

locais = {}

with open(entrada, "r", encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")

    for linha in leitor:
        chave = (
            linha["NR_ZONA"],
            linha["NR_LOCAL_VOTACAO"]
        )

        if chave not in locais:
            locais[chave] = {
                "NR_ZONA": linha["NR_ZONA"],
                "NR_LOCAL_VOTACAO": linha["NR_LOCAL_VOTACAO"],
                "NM_LOCAL_VOTACAO": linha["NM_LOCAL_VOTACAO"],
                "DS_LOCAL_VOTACAO_ENDERECO": linha[
                    "DS_LOCAL_VOTACAO_ENDERECO"
                ],
                "RA": ""
            }

colunas = [
    "NR_ZONA",
    "NR_LOCAL_VOTACAO",
    "NM_LOCAL_VOTACAO",
    "DS_LOCAL_VOTACAO_ENDERECO",
    "RA"
]

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )

    escritor.writeheader()
    escritor.writerows(locais.values())

print("EXTRACAO CONCLUIDA!")
print(f"Total de locais identificados: {len(locais)}")
print(f"Arquivo gerado: {saida}")
