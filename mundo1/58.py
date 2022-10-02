
import random

cont = 0
num = int(input('Digite um número'))

num2 = random.randint(0, 10)  

while num != num2:
    num = int(input('Errou digite outro número'))
    cont += 1

print('Você acertou, total de tentativas {}'.format(cont))
