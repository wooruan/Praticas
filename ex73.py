tabela = ('Palmeiras','Flamengo','Athletico-PR','Fluminense','Bragantino',
       'Bahia','Botafogo','Atlético-MG','Corinthians','Coritiba',
       'Cruzeiro','São Paulo','Vitória','Santos','Grêmio',
       'Internacional','Vasco','Remo','Mirassol','Chapecoense')
i = 0
print ("============================\nOs 5 primeiros colocados são: ", end='')
while True:
    print(f'{tabela[i].upper()}', end='')
    if i == 4:
        break
    print(end=', ')
    i+=1

print ("\n============================\nOs 4 últimos colocados são: ", end='')
qtd = len(tabela)
i = qtd - 4
while True:
    print(f'{tabela[i].upper()}', end='')
    if i == qtd - 1:
        break
    print(end=', ')
    i+=1
print ("\nTimes em ordem alfabética: {}".format(sorted(tabela)))
i = 0
while True:
    if tabela[i] == 'Chapecoense':
        print ("\nA Chapecoense está na {}º Posição".format(i+1))
        break
    else:
        i+=1
