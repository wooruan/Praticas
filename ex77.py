tupla = (str(input("Digite um Palavra: ")),
         str(input("Digite um Palavra: ")),
         str(input("Digite um Palavra: ")),
         str(input("Digite um Palavra: ")))
for p in tupla:
    print (f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print (f'{letra.upper()} ', end='')