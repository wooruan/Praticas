tupla = (int(input("Digite um valor: ")),
         int(input("Digite um valor: ")),
         int(input("Digite um valor: ")),
         int(input("Digite um valor: ")))
print (tupla)
print (f"O valor 9 foi digitado {tupla.count(9)} vezes")
if 3 in tupla:
    print(f'O valor 3 está na {tupla.index(3)+1} posição')
else:
    print('O valor 3 não está na tupla')
print('Os valores pares digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end = ' ')