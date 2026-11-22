
import csv
from pathlib import Path
from collections import Counter

entrada = Path("data/processed/revisao_ra_uibra.csv")
pasta_saida = Path("data/processed")

saida_resumo = pasta_saida / "resumo_zonas_pendentes.csv"
saida_pendentes = pasta_saida / "todos_locais_pendentes.csv"

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)
    colunas = leitor.fieldnames

pendentes = [
    linha for linha in linhas
    if linha["STATUS"] == "PENDENTE"
    and not linha["RA_PROVAVEL"].strip()
]

contagem = Counter(
    linha["NR_ZONA"] for linha in pendentes
)

resumo = sorted(
    contagem.items(),
    key=lambda item: (-item[1], int(item[0]))
)

with open(saida_resumo, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")
    escritor.writerow(["NR_ZONA", "QTD_PENDENTES"])
    escritor.writerows(resumo)

with open(saida_pendentes, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas,
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(pendentes)

print("\nANALISE GERAL CONCLUIDA!")
print(f"Total de locais: {len(linhas)}")
print(f"Sem sugestao: {len(pendentes)}")
print(f"Com RA preenchida ou sugerida: {len(linhas) - len(pendentes)}")

print("\nZONAS COM MAIS PENDENCIAS:")
print("-" * 35)

for zona, quantidade in resumo:
    print(f"Zona {zona:>3}: {quantidade:>3} locais")

print("\nArquivos gerados:")
print(saida_resumo)
print(saida_pendentes)
