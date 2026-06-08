from math import floor
print("=" * 30)
print(f"{"BANCO0":^30}")
print("=" * 30)
qtd = 0
while True:
    valor = float(input('Digite o valor: '))
    resto = valor
    while valor / 50 >= 1:
        resto = valor % 50
        qtd = valor / 50
        print ("Total de {:.0f} cedulas de R$50".format(floor(qtd)))
        valor = resto
    while valor / 20 >= 1:
        resto = valor % 20
        qtd = valor / 20
        print ("Total de {:.0f} cedulas de R$20".format(floor(qtd)))
        valor = resto
    while valor / 10 >= 1:
        resto = valor % 10
        qtd = valor / 10
        print ("Total de {:.0f} cedulas de R$10".format(floor(qtd)))
        valor = resto
    while valor / 1 >= 1:
        resto = valor % 1
        qtd = valor / 1
        print ("Total de {:.0f} cedulas de R$1".format(floor(qtd)))
        valor = resto
    if valor == -1:
        break