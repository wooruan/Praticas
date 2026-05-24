qtd= int(input("Digite a quantidade: "))
t1 = 0
t2 = 1
print(t1, t2, end = " ")
while qtd>2:
    t3 = t1 + t2
    print(t3, end = " ")
    t1 = t2
    t2 = t3
    qtd-=1