valor = float(input("Valor da compra: R$"))
print ("FORMA DE PAGAMENTO:")
print ("[1] à vista dinheiro/cheque")
print ("[2] à vista no cartão")
print ("[3] 2x no cartão")
print ("[4] 3x ou mais no cartao")
opcao=int(input("Qual é a opção: "))
if opcao == 1:
    print ("Sua compra de R${} vai custar R${}".format(valor, valor -(valor * 0.1)))
if opcao == 2:
    print("Sua compra de R${} vai custar R${}".format(valor, valor - (valor * 0.05)))
if opcao == 3:
    print("Sua compra de R${:.2f} vai custar R${:.2f} por mes".format(valor, valor /2))
if opcao == 4:
    qtdparcelas = int(input ("Quantas parcelas? "))
    valorcomjuros = valor * 1.2
    parcela = valorcomjuros / qtdparcelas
    print ("Sua compra será parcelada em {}x vezes de R${:.2f} com JUROS".format(qtdparcelas, parcela))
    print ("Totalizando: R${:.2f}".format(valorcomjuros))