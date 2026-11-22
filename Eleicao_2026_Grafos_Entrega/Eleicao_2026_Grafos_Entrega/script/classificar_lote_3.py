import csv
from collections import Counter
from pathlib import Path

BASE = Path('data/processed/revisao_ra_lote_2.csv')
SAIDA = Path('data/processed/revisao_ra_lote_3.csv')
AUDITORIA = Path('data/processed/auditoria_lote_3.csv')

MAPA = {
 ('2','1252'):('Paranoá','Escola CAIC Santa Paulina; conferir endereço'),
 ('2','1350'):('Paranoá','Quadra 31; conferir endereço'),
 ('2','1619'):('Itapoã','Quadra 378; conferir localização'),
 ('2','1635'):('Lago Norte','Taquari; conferir limite administrativo'),
 ('4','1147'):('Santa Maria','Escola Classe 203; conferir endereço'),
 ('4','1651'):('Santa Maria','Porto Rico; revisar limite'),
 ('4','1694'):('Santa Maria','QR 307; conferir endereço'),
 ('6','1066'):('Planaltina','Avenida Independência'),
 ('6','1074'):('Planaltina','Vila Vicentina'),
 ('6','1082'):('Planaltina','Avenida São Paulo'),
 ('6','1520'):('Planaltina','Vila Nossa Senhora de Fátima'),
 ('6','1600'):('Planaltina','Bairro Nossa Senhora de Fátima'),
 ('6','1716'):('Planaltina','Rua Hugo Lobo'),
 ('9','1236'):('Guará','Colégio Rogacionista; conferir unidade'),
 ('9','1414'):('SIA','SIA Trecho 04'),
 ('10','1023'):('Núcleo Bandeirante','2ª Avenida entreblocos'),
 ('10','1058'):('Núcleo Bandeirante','2ª Avenida entreblocos'),
 ('10','1104'):('Núcleo Bandeirante','3ª Avenida'),
 ('10','1120'):('Candangolândia','SPMS QR 1; conferir endereço'),
 ('10','1147'):('Núcleo Bandeirante','Metropolitana; conferir limite'),
 ('10','1155'):('Park Way','Vargem Bonita Park Way'),
 ('10','1333'):('Núcleo Bandeirante','QRO A; conferir endereço'),
 ('11','1112'):('Plano Piloto','Setor Militar Urbano'),
 ('11','1139'):('Sudoeste/Octogonal','Setor Sudoeste'),
 ('11','1180'):('Plano Piloto','SIG Quadra 08'),
 ('15','1112'):('Taguatinga','QSC 01; conferir endereço'),
 ('15','1180'):('Taguatinga','ECNA 01/02; conferir endereço'),
 ('15','1295'):('Arniqueira','Colônia Agrícola Arniqueira; conferir limite'),
 ('15','1317'):('Águas Claras','Escola La Salle; conferir unidade'),
 ('15','1384'):('Águas Claras','QS 03 Rua 420; conferir limite'),
 ('15','1392'):('Arniqueira','Vila Areal; conferir limite'),
 ('15','1490'):('Águas Claras','Quadra 204; conferir endereço'),
 ('15','1651'):('Taguatinga','Endereço informa Taguatinga Sul; nome menciona Águas Claras'),
 ('16','1309'):('Ceilândia','Setor P Norte'),
 ('16','1333'):('Brazlândia','Escola Classe 05 GB; conferir localização'),
 ('16','1384'):('Brazlândia','EQ 6/8; conferir localização'),
 ('16','1392'):('Brazlândia','Escola Classe 01; conferir localização'),
 ('16','1422'):('Brazlândia','Quadra 38; conferir localização'),
 ('16','1449'):('Brazlândia','Quadra 38; conferir localização'),
 ('16','1490'):('Brazlândia','Centro de Ensino Médio 01; conferir localização'),
 ('16','1600'):('Brazlândia','Quadra 04; conferir localização'),
 ('16','1619'):('Brazlândia','Irmãs Oblatas; conferir localização'),
 ('17','1066'):('Gama','Setor Oeste; conferir endereço'),
 ('17','1422'):('Gama','Setor Leste Industrial'),
 ('18','1031'):('São Sebastião','Quadra 303; conferir endereço'),
 ('18','1040'):('São Sebastião','Bairro São José'),
 ('18','1082'):('São Sebastião','Cerâmica da Benção'),
 ('18','1090'):('São Sebastião','Cerâmica São Paulo; conferir endereço'),
 ('18','1112'):('São Sebastião','Bairro Vila Nova'),
 ('18','1120'):('São Sebastião','Bairro São José'),
 ('18','1139'):('São Sebastião','Residencial Oeste'),
 ('18','1244'):('São Sebastião','Bairro Bela Vista'),
 ('18','1252'):('São Sebastião','Centro Educacional São Bartolomeu; conferir'),
 ('18','1287'):('Jardim Botânico','Estrada do Sol; conferir limite'),
 ('18','1341'):('São Sebastião','Centro Educacional São Francisco; conferir'),
 ('18','1392'):('Jardim Botânico','Complexo da Papuda; conferir limite'),
 ('19','1236'):('Vicente Pires','Colônia Agrícola Vila São José; conferir limite'),
 ('19','1260'):('Taguatinga','Setor G Norte'),
 ('19','1279'):('Vicente Pires','Rua 06 Chácara 276; conferir endereço'),
 ('19','1287'):('Vicente Pires','Rua 06 Chácara 253; conferir endereço'),
 ('19','1295'):('Vicente Pires','Rua 10 Chácara 323; conferir endereço'),
 ('19','1325'):('Vicente Pires','Rua 03 Chácara 82; conferir endereço'),
 ('19','1333'):('Vicente Pires','Rua 07 Chácara 324; conferir endereço'),
 ('20','1210'):('Sol Nascente/Pôr do Sol','Quadra 500 Trecho 01; conferir endereço'),
}

REVISOES = {
 ('10','1422'):('Park Way','Endereço PARK WAY TRECHO 2 QD 6 prevalece sobre nome da escola'),
}

with BASE.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    linhas = list(reader)
    campos = reader.fieldnames

log = []
contagem = Counter()
for linha in linhas:
    chave = (linha['NR_ZONA'].strip(), linha['NR_LOCAL_VOTACAO'].strip())
    anterior = linha['RA_PROVAVEL'].strip()
    if chave in REVISOES:
        ra, motivo = REVISOES[chave]
        linha['RA_PROVAVEL'] = ra
        linha['REGRA_UTILIZADA'] = 'LOTE_3_CONFLITO_REVISAR'
        tipo = 'REVISAO'
    elif chave in MAPA and linha['STATUS'] == 'PENDENTE' and not anterior:
        ra, motivo = MAPA[chave]
        linha['RA_PROVAVEL'] = ra
        linha['REGRA_UTILIZADA'] = 'LOTE_3_REVISAR'
        tipo = 'NOVA_SUGESTAO'
        contagem[ra] += 1
    else:
        continue
    log.append({'NR_ZONA':chave[0], 'NR_LOCAL_VOTACAO':chave[1],
                'NM_LOCAL_VOTACAO':linha['NM_LOCAL_VOTACAO'],
                'ENDERECO':linha['DS_LOCAL_VOTACAO_ENDERECO'],
                'RA_ANTERIOR':anterior, 'RA_NOVA':linha['RA_PROVAVEL'],
                'TIPO':tipo, 'MOTIVO':motivo})

with SAIDA.open('w', encoding='utf-8-sig', newline='') as f:
    w=csv.DictWriter(f,fieldnames=campos,delimiter=';')
    w.writeheader(); w.writerows(linhas)
with AUDITORIA.open('w', encoding='utf-8-sig', newline='') as f:
    w=csv.DictWriter(f,fieldnames=['NR_ZONA','NR_LOCAL_VOTACAO','NM_LOCAL_VOTACAO','ENDERECO','RA_ANTERIOR','RA_NOVA','TIPO','MOTIVO'],delimiter=';')
    w.writeheader(); w.writerows(log)
restantes=sum(l['STATUS']=='PENDENTE' and not l['RA_PROVAVEL'].strip() for l in linhas)
print('LOTE 3 CONCLUIDO')
print('Novas sugestoes:',sum(x['TIPO']=='NOVA_SUGESTAO' for x in log))
print('Revisoes:',sum(x['TIPO']=='REVISAO' for x in log))
print('Sem sugestao:',restantes)
print('Total:',len(linhas))
print('Por RA:',dict(contagem))
print('Base:',SAIDA)
print('Auditoria:',AUDITORIA)
