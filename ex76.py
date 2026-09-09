tupla = ("Lápis", 1.75,
         "Borracha", 2.00,
         "Caderno", 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livros', 34.90)
print(f'{'LISTA DE MATERIAIS':^35}')
print(f'{40*'_'}')
for pos in range (0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}R${tupla[pos+1]:>7}')