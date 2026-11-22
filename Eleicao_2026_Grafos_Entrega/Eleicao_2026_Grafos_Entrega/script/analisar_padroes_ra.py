
import csv
import re
from pathlib import Path
from collections import Counter

entrada = Path("data/processed/locais_ra_sugeridas.csv")
saida = Path("data/processed/revisao_ra.csv")

regras = {
    "Ceilândia": r"\b(EQNM|EQNN|EQNO|EQNL|EQNP|QNJ|QNL|QNN|QNP|QNR|QNM)\b",
    "Plano Piloto": r"\b(SQS|SQN|SGAS|SGAN|SEPN|SEPS|EQS|EQN)\b",
    "Taguatinga": r"\b(QND|QNG|QNB|QNC|QNF|QNA|QSA|QSB|QSD|QSE)\b",
    "Lago Sul": r"\bSHIS\b",
    "Lago Norte": r"\bSHIN\b",
    "Guará": r"\b(SRIA|QE)\b",
    "Cruzeiro": r"\b(SHCES|SRES)\b"
}

contagem = Counter()

with open(entrada, "r", encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)

for linha in linhas:
    linha["RA_PROVAVEL"] = ""
    linha["REGRA_UTILIZADA"] = ""

    if linha["STATUS"] != "PENDENTE":
        continue

    endereco = linha["DS_LOCAL_VOTACAO_ENDERECO"].upper()

    encontradas = []

    for ra, padrao in regras.items():
        if re.search(padrao, endereco):
            encontradas.append(ra)

    if len(encontradas) == 1:
        linha["RA_PROVAVEL"] = encontradas[0]
        linha["REGRA_UTILIZADA"] = "PADRAO_ENDERECO"
        contagem[encontradas[0]] += 1

    elif len(encontradas) > 1:
        linha["REGRA_UTILIZADA"] = "AMBIGUO"

    else:
        linha["REGRA_UTILIZADA"] = "SEM_CORRESPONDENCIA"

saida.parent.mkdir(parents=True, exist_ok=True)

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=linhas[0].keys(),
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(linhas)

print("ANALISE CONCLUIDA!")
print("-" * 45)

for ra, quantidade in contagem.most_common():
    print(f"{ra}: {quantidade} sugestoes")

print("-" * 45)
print(f"Total de sugestoes: {sum(contagem.values())}")
print(f"Arquivo gerado: {saida}")
