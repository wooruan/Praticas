num1 = int(input("digite um numero: "))
resto = num1
if num1 >= 1:
    resto = resto % 2
    num1 = num1 // 2
    print(num1, resto)
    if num1 >=1:
        resto = num1 % 2
        num1 = num1 // 2
        print(num1, resto)
        if num1 >=1:
            resto = num1 % 2
            num1 = num1 // 2
            print(num1, resto)
            if num1 >=1:
                resto = num1 % 2
                num1 = num1 // 2
                print(num1, resto)
                if num1 >=1:
                    resto = num1 % 2
                    num1 = num1 // 2
                    print(num1, resto)
