tabela = ('Palmeiras','Flamengo','Athletico-PR','Fluminense','Bragantino',
       'Bahia','Botafogo','Atlético-MG','Corinthians','Coritiba',
       'Cruzeiro','São Paulo','Vitória','Santos','Grêmio',
       'Internacional','Vasco','Remo','Mirassol','Chapecoense')
i = 0
print ("Os 5 primeiros colocados são: {}".format(tabela[0:5]))

print ("Os 4 últimos colocados são: {}".format(tabela[-4:]))

print ("Times em ordem alfabética: {}".format(sorted(tabela)))

print ("A Chapecoense está na {}º Posição".format(tabela.index('Chapecoense')+1))
