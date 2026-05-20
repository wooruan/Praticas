import random
pri = str(input ("Primeiro aluno: "))
seg = str(input ("Segundo aluno: "))
ter = str(input ("Terceiro aluno: "))
alunos = [seg, ter, pri]
res = random.choice(alunos)
print (res)
print (random.choice(alunos))