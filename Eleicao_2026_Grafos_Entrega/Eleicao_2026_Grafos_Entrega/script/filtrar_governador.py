
import csv
from pathlib import Path

entrada = Path("data/raw/votacao_secao_2026_DF/votacao_secao_2026_DF.csv")
saida = Path("data/processed/governador_df_turno1.csv")

colunas = [
    "NR_TURNO",
    "NR_ZONA",
    "NR_SECAO",
    "NR_LOCAL_VOTACAO",
    "NM_LOCAL_VOTACAO",
    "DS_LOCAL_VOTACAO_ENDERECO",
    "NR_VOTAVEL",
    "NM_VOTAVEL",
    "QT_VOTOS"
]

total_registros = 0
total_votos = 0

saida.parent.mkdir(parents=True, exist_ok=True)

with open(entrada, "r", encoding="latin-1", newline="") as origem:
    leitor = csv.DictReader(origem, delimiter=";")

    with open(saida, "w", encoding="utf-8-sig", newline="") as destino:
        escritor = csv.DictWriter(destino, fieldnames=colunas, delimiter=";")
        escritor.writeheader()

        for linha in leitor:
            if linha["DS_CARGO"] == "Governador" and linha["NR_TURNO"] == "1":
                escritor.writerow({
                    coluna: linha[coluna] for coluna in colunas
                })

                total_registros += 1
                total_votos += int(linha["QT_VOTOS"])

print("FILTRAGEM CONCLUIDA!")
print(f"Registros encontrados: {total_registros}")
print(f"Votos contabilizados: {total_votos}")
print(f"Arquivo gerado: {saida}")
