sal = int(input("Digite o salario: "))
if sal > 1250:
    print ("o aumento será de 10%, totalizando: {}$".format(sal*1.10))
else:
    print ("o aumento será de 15%, totalizando: {}$".format(sal*1.15))