i = 0
num = int(input("Digite um numero: "))
for c in range (1,num+1):
    if num % c == 0:
        print(c)
        i += 1
if i == 2:
    print("Número Primo")
else:
    print("Número nao primo")