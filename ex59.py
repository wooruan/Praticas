num1 = float (input("Numero 1: "))
num2 = float (input("Numero 2: "))
opcao = 0
while opcao != 5:
    opcao = int(input(("\n[1]Somar\n[2]Multiplicar\n[3]Maior Valor\n[4]Novos números\n[5]Sair do programa\n :")))
    if opcao == 1:
        print ("Soma: {}".format(num1 + num2))
    elif opcao == 2:
        print ("Multiplicação: {}".format(num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print ("Maior: {}".format(num1))
        elif num1 < num2:
            print ("Maior: {}".format(num2))
        else:
            print("Os numeros sao iguais")
    elif opcao == 4:
        num1 = float(input("Novo numero 1: "))
        num2 = float(input("Novo numero 2: "))
    elif opcao == 5:
        print ("Programa Finalizado")
    else:
        print("Opcao invalida, tente novamente")