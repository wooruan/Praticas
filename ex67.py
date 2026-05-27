while True:
    num = int(input('Digite um numero: '))
    if num < 0:
        break
    i = 1
    while i<=10:
        print(f'{num:^3} x {i:2} = {i*num}')
        i+=1