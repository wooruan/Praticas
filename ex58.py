import random
i=0
numero = 0
sorteado = -1
while (numero != sorteado):
    numero = int(input("\nEstou pensando em um número entre 0 e 5, tente adivinhar: \n"))
    nums = [0,1,2,3,4,5]
    sorteado = random.choice(nums)
    i+=1
    if numero == sorteado:
        print("----------")
        print ("parabens")
        v = 1
    else:
        print ("errou {} \n----------". format(sorteado))

print ("Palpites: {}".format(i))