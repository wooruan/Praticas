qtd = 3
resp = 'S'
num = i = soma = maior = menor = 0
while resp == 'S':
    while qtd>0:
        print ("__"*10)
        num = float(input("Digite um valor: "))
        i+=1
        soma += num
        print("Média atual: {}".format(soma/i))
        if i == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        print ("\nMaior valor: {}\nMenor Valor: {}\n".format(maior, menor))
        qtd-=1
    print ("=*="*15)
    resp = str(input("Voce quer digitar mais um valor [S/N]?  ")).strip().upper()
    if resp == 'S':
        qtd+=1