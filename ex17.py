import math
ca = float((input("qual o cumprimento do cateto adjascente: ")))
co = float((input("qual o cumprimento do oposto: ")))
h = (ca ** (2/1) + co ** (2/1)) ** (1/2)
print (h)
hi = math.hypot(ca, co)
print ("o cumprimento da ipotenusa é: {:.2f} ou {:.2f}".format(h, hi))
5
