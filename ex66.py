soma = cont = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont +=1
    soma += num
print(f'numeros digitados: {cont}, soma de todos: {soma} ')