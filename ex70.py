total = maior = barato =0
nomebarato = ''
i = 0
print ("======SUPERCEI======")
while True:
    nome = str(input("Nome do Produto: "))
    preco = float (input("Valor do Produto: "))
    total = total + preco
    if preco > 1000 :
        maior+=1
    if i == 0 or preco < barato:
        barato = preco
        nomebarato = nome
    i+=1
    resp = str(input("Quer Continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print("="*20)
print(f'O total da compra foi R${total:.2f}')
print('Temos {} produto custando mais de R$1000.00'.format(maior))
print('O produto mais barato foi {} custando R${:.2f}'.format(nomebarato, barato))
