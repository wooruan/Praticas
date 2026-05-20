n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))
n3 = int(input("digite mais um numero: "))
maior = 0
menor = 0
menor2 = 0

if n1 > n2 and n1 > n3:
    print("o maior valor é: {}".format(n1))
    maior = n1
if n2 > n1 and n2 > n3:
    print("o maior valor é: {}".format(n2))
    menor = n2
if n3 > n1 and n3 > n2:
    print("o maior valor é: {}".format(n3))
    menor = n3

if n1 < n2 and n1 < n3:
    print("o menor valor é: {}".format(n1))
    maior = n1
if n2 < n1 and n2 < n3:
    print("o menor valor é: {}".format(n2))
    menor = n2
if n3 < n1 and n3 < n2:
    print("o menor valor é: {}".format(n3))
    menor = n3