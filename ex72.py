ext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    resp = int(input("Digite um numero: "))
    while resp < 0 or resp > 20:
        resp = int(input('Tente Novamente. Digite um numero entre 0 e 20: '))
    print ("Voce Digitou {} ".format(ext[resp]))