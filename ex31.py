viagem = int(input("Qual a distancia da viagem: em km "))
if viagem > 200:
    print(" o valor será 0,45$ x {}:  {}$". format (viagem, viagem * 0.45))
else:
    print (" o valor será 0,50$ x {}:  {}$". format (viagem, viagem * 0.50))
