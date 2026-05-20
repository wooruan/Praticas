from datetime import date

anoatual = date.today().year
anonas = int(input("Digite seu ano de nascimento: "))
idade = anoatual - anonas
print ("quem nasceu em {} tem {} anos em {}".format(anonas, idade, anoatual))
if idade < 18:
    print("falta {} anos para se alistar".format(18-idade))
    print("seu alistamento será em {}".format(anonas + 18))
elif idade == 18:
    print ("voce tem {} anos e deve se alistar esse ano".format(idade))
else :
    print("voce tem {} anos e deveria ter se alistado em {}, ha {} anos atras".format(idade, anonas+18, idade-18))