print("Digite 999 para parar   ")
num = 0
i = 0
soma = 0
while num != 999:
    num = int(input("digite um numero: "))
    if num != 999:
        soma = soma + num
        i += 1
print ("Quantidade de numeros digitados: {}\nSoma de todos os numeros: {}".format(i, soma))