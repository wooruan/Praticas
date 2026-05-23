import datetime
data = datetime.date.today().year
pessoa = 0
maior = 0
menor = 0
for c in range(1, 8, 1):
    pessoa = int(input("Qual ano a {}º pessoa nasceu: ".format(c)))
    if  data - pessoa >= 18:
        maior += 1
    else:
        menor += 1
print ("temos {} maiores de idade e {} menores de idade".format(maior, menor))