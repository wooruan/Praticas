import random
i = 0
while True:
    tupla = []
    tupla[i] = random.randint(0, 5)
    i += 1
    if i == 5:
        break
print (tupla)
maior = 0
menor = tupla[0]
i = 0
while True:
    if tupla[i] > maior:
        maior = tupla[i]
    if tupla[i] < menor:
        menor = tupla[i]
    i += 1
    if i == 5:
        break

print ("O maior: {}\nO menor: {}".format(maior, menor))