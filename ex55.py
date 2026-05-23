menor = 0
maior = 0
p = 0
for c in range (1, 6):
    p = float(input("Qual o peso da {}º pessoa: ".format(c)))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print(maior, "  ", menor)