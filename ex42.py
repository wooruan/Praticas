r1 = float(input('Primeiro segmento: '))
r2= float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1< r2 + r3 and r2< r1+ r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triangulo!')
    if r1 == r2 == r3:
        print("O triangulo é um  EQUILATERO!")
    elif r1 != r2 != r3 != r1:
        print("O triangulo é um ESCALENO!")
    else:
        print("O triangulo é um ISOSCELES!")
else:
    print('Os seamentos acima NÃO PODEM FORMAR triângulo')