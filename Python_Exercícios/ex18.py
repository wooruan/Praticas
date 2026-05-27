import math
angulo = float(input("digite o ANGULO"
                     ": "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print (" O Angulo tem o seno de {:.2f}".format(seno))
print (" O Angulo tem o cosseno de {:.2f}".format(cosseno))
print (" O Angulo tem a tangente de {:.2f}".format(tangente))
