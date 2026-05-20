valorcasa = float(input("Qual o valor da casa: "))
salario = float(input("Digite o salário: "))
anospagar = int(input("Em quantos anos quer pagar: "))
prestação = valorcasa / (anospagar * 12)
print (prestação)

if prestação <= salario * 0.3:
    print("Emprestimo aprovado com sucesso!")
    print("Voce pagara {:.2f}$ por mes, sendo {:.2f}$ por ano".format(prestação, prestação * 12))
else:
    print("Emprestimo NEGADO, seu salário é menor que 30% do valor da prestação ")