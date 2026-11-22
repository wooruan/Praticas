
import csv
from collections import defaultdict
from pathlib import Path

pasta = Path("data/processed")

arquivo_locais = pasta / "revisao_ra_consolidada_preliminar.csv"
arquivo_votos = pasta / "governador_df_turno1.csv"

def ler_csv(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))

locais = ler_csv(arquivo_locais)
votos = ler_csv(arquivo_votos)

mapa = {}

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

    mapa[chave] = {
        "categoria": categoria,
        "regra": regra or "SEM_REGRA"
    }

totais = defaultdict(int)
totais_validos = defaultdict(int)
locais_por_categoria = defaultdict(set)
sem_correspondencia = set()

for voto in votos:
    chave = (
        voto["NR_ZONA"].strip(),
        voto["NR_LOCAL_VOTACAO"].strip()
    )

    if chave not in mapa:
        sem_correspondencia.add(chave)
        continue

    categoria = mapa[chave]["categoria"]
    quantidade = int(voto["QT_VOTOS"])

    totais[categoria] += quantidade
    locais_por_categoria[categoria].add(chave)

    if voto["NR_VOTAVEL"].strip() not in {"95", "96"}:
        totais_validos[categoria] += quantidade

total_geral = sum(totais.values())

print("AUDITORIA DO IMPACTO NOS VOTOS")
print("-" * 65)

for categoria in sorted(totais):
    percentual = (
        100 * totais[categoria] / total_geral
        if total_geral else 0
    )

    print(f"\n{categoria}")
    print(f"Locais com votos: {len(locais_por_categoria[categoria])}")
    print(f"Votos registrados: {totais[categoria]}")
    print(f"Votos validos: {totais_validos[categoria]}")
    print(f"Participacao no total: {percentual:.2f}%")

print("\n" + "-" * 65)
print(f"Total de votos registrados: {total_geral}")
print(f"Locais sem correspondencia: {len(sem_correspondencia)}")
