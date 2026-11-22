
import csv
from collections import defaultdict
from pathlib import Path

pasta = Path("data/processed")

arquivo_votos = pasta / "governador_df_turno1.csv"
arquivo_locais = pasta / "revisao_ra_consolidada_preliminar.csv"

saida = pasta / "votos_governador_por_ra.csv"
auditoria = pasta / "auditoria_votos_ra.csv"

def ler_csv(caminho):
    with open(caminho, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))

votos = ler_csv(arquivo_votos)
locais = ler_csv(arquivo_locais)

mapa_locais = {}

for local in locais:
    chave = (
        local["NR_ZONA"].strip(),
        local["NR_LOCAL_VOTACAO"].strip()
    )

    ra = (
        local["RA"].strip()
        or local["RA_PROVAVEL"].strip()
    )

    if chave in mapa_locais:
        raise ValueError(f"Local duplicado: {chave}")

    mapa_locais[chave] = {
        "ra": ra,
        "status": local["STATUS"].strip()
    }

totais = defaultdict(int)
problemas = defaultdict(int)

for voto in votos:
    chave = (
        voto["NR_ZONA"].strip(),
        voto["NR_LOCAL_VOTACAO"].strip()
    )

    local = mapa_locais.get(chave)

    if local is None or not local["ra"]:
        problemas[chave] += 1
        continue

    grupo = (
        local["ra"],
        voto["NR_VOTAVEL"].strip(),
        voto["NM_VOTAVEL"].strip()
    )

    totais[grupo] += int(voto["QT_VOTOS"])

with open(saida, "w", encoding="utf-8-sig", newline="") as f:
    escritor = csv.writer(f, delimiter=";")
    escritor.writerow([
        "RA", "NR_VOTAVEL", "NM_VOTAVEL", "QT_VOTOS"
    ])

    for chave, quantidade in sorted(totais.items()):
        escritor.writerow([*chave, quantidade])

with open(auditoria, "w", encoding="utf-8-sig", newline="") as f:
    escritor = csv.writer(f, delimiter=";")
    escritor.writerow([
        "NR_ZONA", "NR_LOCAL_VOTACAO", "REGISTROS_SEM_RA"
    ])

    for chave, quantidade in sorted(problemas.items()):
        escritor.writerow([*chave, quantidade])

print("AGRUPAMENTO CONCLUIDO")
print("-" * 40)
print(f"Registros de votos: {len(votos)}")
print(f"Locais cadastrados: {len(mapa_locais)}")
print(f"Grupos RA/candidato: {len(totais)}")
print(f"Locais sem correspondencia: {len(problemas)}")
print(f"Arquivo: {saida}")
print(f"Auditoria: {auditoria}")
