from datetime import date
anonasc=int(input("digite seu ano de nascimento: "))
idade=date.today().year - anonasc

if idade <= 9:
    print("o atleta tem {} anos".format (idade))
    print("CLASSIFICAÇÃO: Mirim " )
elif idade <= 14:
    print("o atleta tem {} anos".format (idade))
    print("CLASSIFICAÇÃO: Infantil " )
elif idade <= 19:
    print("o atleta tem {} anos".format (idade))
    print("CLASSIFICAÇÃO: Junior " )
elif idade <= 25:
    print("o atleta tem {} anos".format (idade))
    print("CLASSIFICAÇÃO: Senior " )
elif idade > 25:
    print("o atleta tem {} anos".format (idade))
    print("CLASSIFICAÇÃO: Master " )