import random

print ("PEDRA PAPEL E TESOURA")
print("[1]PEDRA \n[2]PAPEL \n[3]TESOURA")
escolhas = ['Pedra', 'Papel', 'Tesoura']
pc = random.randint(0,2)
jogador = int(input("Qual a sua jogada? "))
if jogador == 1 and pc == 1 or jogador == 2 and pc == 2 or jogador == 3 and pc == 3:
    print ("Empate, maquina escolheu {}".format(escolhas[pc]))
if jogador == 1 and pc == 2 or jogador == 2 and pc == 3 or jogador == 3 and pc == 1:
    print ("Perdeu, maquina escolheu {}".format(escolhas[pc]))
if jogador == 1 and pc == 3 or jogador == 2 and pc == 1 or jogador == 3 and pc == 2:
    print ("Ganhou, maquina escolheu {}".format(escolhas[pc]))