
import csv
from pathlib import Path

entrada = Path("data/processed/revisao_ra_lote_2.csv")
saida = Path("data/processed/revisao_final.csv")

with open(entrada, encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    linhas = list(leitor)

revisao = []

for linha in linhas:
    sem_ra = (
        linha["STATUS"] == "PENDENTE"
        and not linha["RA_PROVAVEL"].strip()
    )

    sugestao_recente = (
        linha["REGRA_UTILIZADA"] in [
            "LOTE_GERAL_REVISAR",
            "LOTE_2_REVISAR"
        ]
    )

    if sem_ra or sugestao_recente:
        revisao.append({
            "NR_ZONA": linha["NR_ZONA"],
            "NR_LOCAL_VOTACAO": linha["NR_LOCAL_VOTACAO"],
            "NM_LOCAL_VOTACAO": linha["NM_LOCAL_VOTACAO"],
            "DS_LOCAL_VOTACAO_ENDERECO":
                linha["DS_LOCAL_VOTACAO_ENDERECO"],
            "RA_PROVAVEL": linha["RA_PROVAVEL"],
            "REGRA_UTILIZADA": linha["REGRA_UTILIZADA"]
        })

revisao.sort(
    key=lambda x: (
        int(x["NR_ZONA"]),
        int(x["NR_LOCAL_VOTACAO"])
    )
)

with open(saida, "w", encoding="utf-8-sig", newline="") as arquivo:
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=list(revisao[0].keys()),
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(revisao)

print("\nREVISAO FINAL GERADA!")
print(f"Locais para revisar: {len(revisao)}")
print(f"Arquivo: {saida}")
