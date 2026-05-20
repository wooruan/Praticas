import random
while (1>0):
    numero = int(input("\n      Estou pensando em um número entre 0 e 5, tente adivinhar: "))
    nums = [0,1,2,3,4,5]
    sortead0 = random.choice(nums)

    if numero == sortead0:
        print ("    parabens")
    else:
        print ("errou {} \n". format(sortead0))
