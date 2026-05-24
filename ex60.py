num = int(input("Digite um numero: "))
i = a = num
fator1 = 1
fator = 1
while num > 1:
    fator = fator * num
    num -= 1
print ("O fatorial de {} é {} ".format (i, fator))

for c in range(i, 0, -1):
    fator1 = fator1 * c
print ("O fatorial de {} é {}".format(a,fator1))