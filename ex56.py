soma = 0
maior = 0
nmaior = 0
i = 0
b=0
for c in range (1, 5):
    print ("-=-=-=-=-=-=-=-")
    print("{}º Pessoa".format(c))
    nome = str(input("nome: "))
    idade = int(input("idade: "))
    sexo = str(input("Sexo[M/F]: ")).strip().upper()
    soma = soma + idade
    if sexo == "M":
        if idade > maior:
            maior = idade
            nmaior = nome
    if sexo == "F":
        if idade < 20:
            i +=1
    b +=1
print (" A media de idade do grupo é igual a {} ".format(soma/b))
print (" O homem mais velho é {} e tem {} anos".format(nmaior, maior))
print (" Ao todo {} mulheres tem menos de 20 anos".format(i))