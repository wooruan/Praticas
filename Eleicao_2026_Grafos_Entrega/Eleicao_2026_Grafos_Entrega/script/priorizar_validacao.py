
import csv
from collections import defaultdict
from pathlib import Path

pasta = Path("data/processed")

arquivo_locais = pasta / "revisao_ra_consolidada_preliminar.csv"
arquivo_votos = pasta / "governador_df_turno1.csv"
saida = pasta / "prioridade_validacao.csv"

def ler_csv(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))

locais = ler_csv(arquivo_locais)
votos = ler_csv(arquivo_votos)

totais_por_local = defaultdict(int)

for voto in votos:
    chave = (
        voto["NR_ZONA"].strip(),
        voto["NR_LOCAL_VOTACAO"].strip()
    )

    totais_por_local[chave] += int(voto["QT_VOTOS"])

resultado = []

for local in locais:
    chave = (
        local["NR_ZONA"].strip(),
        local["NR_LOCAL_VOTACAO"].strip()
    )

    regra = local["REGRA_UTILIZADA"].strip()

    if not regra:
        categoria = "SEM_REGRA"
    elif regra.startswith("LOTE_") or regra == "REVISAO_MANUAL_NAO_VALIDADA":
        categoria = "LOTES_E_HIPOTESES"
    else:
        categoria = "ENDERECO_E_LOCALIDADE"

    resultado.append({
        "NR_ZONA": chave[0],
        "NR_LOCAL_VOTACAO": chave[1],
        "NM_LOCAL_VOTACAO": local["NM_LOCAL_VOTACAO"],
        "ENDERECO": local["DS_LOCAL_VOTACAO_ENDERECO"],
        "RA_ATUAL": local["RA"].strip() or local["RA_PROVAVEL"].strip(),
        "STATUS": local["STATUS"],
        "REGRA_UTILIZADA": regra or "SEM_REGRA",
        "CATEGORIA": categoria,
        "QT_VOTOS": totais_por_local[chave]
    })

resultado.sort(
    key=lambda item: item["QT_VOTOS"],
    reverse=True
)

with open(saida, "w", encoding="utf-8-sig", newline="") as f:
    escritor = csv.DictWriter(
        f,
        fieldnames=resultado[0].keys(),
        delimiter=";"
    )
    escritor.writeheader()
    escritor.writerows(resultado)

print("PRIORIZACAO CONCLUIDA")
print("-" * 45)
print(f"Locais analisados: {len(resultado)}")
print(f"Arquivo: {saida}")

print("\n10 LOCAIS COM MAIS VOTOS")
print("-" * 45)

for local in resultado[:10]:
    print(
        f"Zona {local['NR_ZONA']} | "
        f"Local {local['NR_LOCAL_VOTACAO']} | "
        f"{local['RA_ATUAL']} | "
        f"{local['QT_VOTOS']} votos"
    )
