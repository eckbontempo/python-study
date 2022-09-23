import random

n = int(input('Digite um número'))
m = random.randrange(0, 5) 

print('Você ganhou' if n == m else 'Você perdeu')
print('Computador disse', m)