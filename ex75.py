tupla = (int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")), )
print (tupla)
i = 0
a = 0
for c in tupla:
    if c == 9:
        i += 1
    if c % 2 == 0:
        print (f'O valor {c} é par')
    if c == 3 and a == 0:
        print (f'O valor 3 está na {tupla.index(3)+1}º posição')
        a+=1
print (f"O valor 9 apareceu {i} vezes")
