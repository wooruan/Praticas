
print("=" * 30)
print(f"{"BANCO0":^30}")
print("=" * 30)
ced = 50
total = 0
totalced = 0
valor = float(input('Digite o valor: '))
while True:

    if valor >= ced:
        valor -= ced
        totalced+=1
    else:
        if totalced > 0:
            print ("Total de {} cedulas de R${}".format(totalced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if valor == 0:
            break

