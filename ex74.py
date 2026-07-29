import random

tupla = (random.randint(0, 5),random.randint(0, 5),random.randint(0, 5),random.randint(0, 5),random.randint(0, 5))
print("Tupla: ", end='')
for c in tupla:
    print(f"{c} ", end='')
print ("\nO maior: {}\nO menor: {}".format(max(tupla),min(tupla)))