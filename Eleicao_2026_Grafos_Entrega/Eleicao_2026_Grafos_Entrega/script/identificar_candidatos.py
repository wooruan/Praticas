
import csv
from collections import defaultdict

arquivo = "data/processed/governador_df_turno1.csv"

votos = defaultdict(int)
registros = defaultdict(int)

with open(arquivo, "r", encoding="utf-8-sig", newline="") as csvfile:
    leitor = csv.DictReader(csvfile, delimiter=";")

    for linha in leitor:
        numero = linha["NR_VOTAVEL"]
        nome = linha["NM_VOTAVEL"]
        quantidade = int(linha["QT_VOTOS"])

        chave = (numero, nome)

        votos[chave] += quantidade
        registros[chave] += 1

print("RESULTADO DA VOTACAO PARA GOVERNADOR - 1 TURNO")
print("-" * 65)

total = sum(votos.values())

for (numero, nome), quantidade in sorted(
    votos.items(),
    key=lambda item: item[1],
    reverse=True
):
    percentual = quantidade / total * 100 if total else 0

    print(f"Numero: {numero}")
    print(f"Nome: {nome}")
    print(f"Votos: {quantidade}")
    print(f"Percentual do total: {percentual:.2f}%")
    print(f"Registros: {registros[(numero, nome)]}")
    print("-" * 65)

print(f"TOTAL GERAL: {total} votos")
