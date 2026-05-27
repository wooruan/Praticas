import random
while True:
    comp = random.randint(0,10)
    print('_'*50)
    num = int(input('Digite um numero: '))
    jog = str(input('Par ou Impar [P/I]: ')).strip().upper()
    print('_'*50)
    print (f'O computador jogou {comp} e o jogador jogou {num}.', end='')
    soma = comp + num
    if soma % 2 == 0:
        print (' Deu PAR')
        if jog == 'P':
            print('VOCE VENCEU')
        else:
            print('VOCE PERDEU')
            break
    elif soma % 2 != 0:
        print(' Deu IMPAR')
        if jog == 'I':
            print('VOCE VENCEU')
        else:
            print('VOCE PERDEU')
            break