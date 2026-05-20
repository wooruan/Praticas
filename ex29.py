print("Qual a velocidade do carro? (KM) ")
vel = int(input())
if vel > 80:
    print(" o valor da multa será 7$ * {} = {}".format (vel-80, (vel- 80) *7))
else:
    print ("Não multado")