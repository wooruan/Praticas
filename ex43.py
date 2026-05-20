altura = float(input("Altura(m): "))
peso = float(input("Peso(Kg): "))
imc = peso / (altura**2)
print ("O imc dessa pessoa é: {:.1f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("Obesidade")
else :
    print("Obesidade morbida")