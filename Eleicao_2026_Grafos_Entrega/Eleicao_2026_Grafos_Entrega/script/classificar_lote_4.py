import csv
from collections import Counter
from pathlib import Path

BASE = Path('data/processed/revisao_ra_lote_3.csv')
SAIDA = Path('data/processed/revisao_ra_lote_4.csv')
AUDITORIA = Path('data/processed/auditoria_lote_4.csv')
PENDENTES = Path('data/processed/pendentes_apos_lote_4.csv')

MAPA = {
 ('2','1317'):('Paranoá','Alto Interlagos/Altiplano Leste; conferir limites'),
 ('2','1538'):('Lago Norte','CA 06; confirmar unidade e endereço'),
 ('2','1546'):('Paranoá','Entrelagos/DF-250; conferir limites'),
 ('2','1627'):('Paranoá','Sobradinho dos Melos/DF-250; conferir limites'),
 ('4','1597'):('Santa Maria','DVO/Cidade Nova; conferir limites'),
 ('5','1309'):('Fercal','Catingueiro/DF-205 Oeste; conferir limites'),
 ('5','1317'):('Fercal','Córrego do Ouro/DF-205; conferir limites'),
 ('5','1350'):('Sobradinho II','Engenho Velho/DF-150; conferir limites'),
 ('5','1422'):('Sobradinho II','Lago Oeste; conferir limites'),
 ('5','1490'):('Fercal','Boa Vista/DF-205 Oeste; conferir limites'),
 ('5','1686'):('Sobradinho II','Vila Basevi; conferir limites'),
 ('5','1732'):('Sobradinho II','Vila Rabelo; conferir limites'),
 ('5','1740'):('Fercal','Estrada da Fercal; conferir limites'),
 ('5','1821'):('Fercal','Queima Lençol; conferir limites'),
 ('6','1171'):('Planaltina','ETA 44/Embrapa; conferir limites'),
 ('6','1210'):('Planaltina','Núcleo rural Monjolo; conferir limites'),
 ('6','1228'):('Planaltina','Núcleo rural Taquara; conferir limites'),
 ('6','1252'):('Planaltina','Núcleo rural Pipiripau; conferir limites'),
 ('6','1287'):('Planaltina','DF-128 Bica do DER; conferir limites'),
 ('6','1295'):('Planaltina','Núcleo rural Santos Dumont; conferir limites'),
 ('6','1481'):('Planaltina','Núcleo rural Tabatinga; conferir limites'),
 ('6','1490'):('Planaltina','Núcleo rural Rio Preto; conferir limites'),
 ('6','1562'):('Planaltina','Estância III; conferir limites'),
 ('6','1686'):('Planaltina','Núcleo rural Jardim Morumbi; conferir limites'),
 ('6','1694'):('Planaltina','Núcleo rural Rajadinha; conferir limites'),
 ('6','1759'):('Planaltina','Vale do Sol/DF-134; conferir limites'),
 ('11','1104'):('Plano Piloto','Vila do RCG; conferir localização'),
 ('15','1309'):('Taguatinga','Setor C 07; conferir localização'),
 ('16','1171'):('Brazlândia','Núcleo rural Boa Esperança; conferir limites'),
 ('16','1341'):('Brazlândia','Almécegas/DF-206; conferir limites'),
 ('16','1350'):('Brazlândia','Curralinho/BR-080; conferir limites'),
 ('16','1473'):('Brazlândia','Vendinha/BR-080; conferir limites'),
 ('16','1481'):('Brazlândia','Chapadinha/DF-240; conferir limites'),
 ('16','1520'):('Brazlândia','Bucanhão/DF-240; conferir limites'),
 ('16','1538'):('Brazlândia','Rodeador/DF-430; conferir limites'),
 ('17','1180'):('Gama','Núcleo rural Casa Grande; conferir limites'),
 ('18','1023'):('São Sebastião','Nova Betânia/BR-251; conferir limites'),
 ('18','1317'):('Paranoá','Núcleo rural Jardim II/DF-285; conferir limites'),
 ('18','1368'):('Paranoá','Café sem Troco/DF-130; conferir limites'),
 ('18','1414'):('Paranoá','Lamarão/DF-285; endereço menciona Paranoá'),
}

with BASE.open(encoding='utf-8-sig', newline='') as f:
    leitor = csv.DictReader(f, delimiter=';')
    linhas = list(leitor)
    campos = leitor.fieldnames

log = []
contagem = Counter()
for linha in linhas:
    chave = (linha['NR_ZONA'].strip(), linha['NR_LOCAL_VOTACAO'].strip())
    if chave not in MAPA or linha['RA'].strip() or linha['RA_PROVAVEL'].strip():
        continue
    ra, motivo = MAPA[chave]
    linha['RA_PROVAVEL'] = ra
    linha['REGRA_UTILIZADA'] = 'LOTE_4_HIPOTESE_VALIDAR'
    contagem[ra] += 1
    log.append({
        'NR_ZONA': chave[0], 'NR_LOCAL_VOTACAO': chave[1],
        'NM_LOCAL_VOTACAO': linha['NM_LOCAL_VOTACAO'],
        'ENDERECO': linha['DS_LOCAL_VOTACAO_ENDERECO'],
        'RA_SUGERIDA': ra, 'JUSTIFICATIVA': motivo,
        'STATUS_VALIDACAO': 'NAO_VALIDADO'
    })

with SAIDA.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=campos, delimiter=';')
    w.writeheader(); w.writerows(linhas)
with AUDITORIA.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(log[0].keys()), delimiter=';')
    w.writeheader(); w.writerows(log)
pendentes = [l for l in linhas if not l['RA'].strip() and not l['RA_PROVAVEL'].strip()]
with PENDENTES.open('w', encoding='utf-8-sig', newline='') as f:
    campos_p = ['NR_ZONA','NR_LOCAL_VOTACAO','NM_LOCAL_VOTACAO','DS_LOCAL_VOTACAO_ENDERECO']
    w = csv.DictWriter(f, fieldnames=campos_p, delimiter=';')
    w.writeheader(); w.writerows({c:l[c] for c in campos_p} for l in pendentes)

print('LOTE 4 CONCLUIDO')
print('Novas hipoteses (nao validadas):', len(log))
print('Sem sugestao:', len(pendentes))
print('Total:', len(linhas))
print('Por RA:', dict(contagem))
print('Base:', SAIDA)
print('Auditoria:', AUDITORIA)
print('Pendentes:', PENDENTES)
