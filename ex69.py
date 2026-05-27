total = homens = mulhermenos = idade = 0

while True:
    escolha = sexo = ''
    print('='*20,'\nCADASTRO\n','='*20)
    idade = int(input('Idade: '))
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo[F/M]: ')).strip().upper()
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Quer Continuar? [S/N]: ')).strip().upper()

    if idade >= 18:
        total +=1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulhermenos +=1

    if escolha == 'N':
        print("=====FIM=====")
        print (f'Total de pessoas com mais de 18 anos: {total}')
        print (f'Ao todo temos {homens} homens cadastrados')
        print (f'E temos {mulhermenos} mulheres com menos de 20 anos')
        break