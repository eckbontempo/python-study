import random

n1 =  input('Nome aluno 1')
n2 =  input('Nome aluno 2')
n3 =  input('Nome aluno 3')
n4 =  input('Nome aluno 4')

list = [n1, n2, n3, n4]
random.shuffle(list)

print(list)
