import random 

contador = 0
pc = random.randint(1,10)
n = int(input('Digite um valor: '))

while n != pc:
    n = int(input('Errou mizeravi! Digite outro número: '))
    contador += 1 
print('Acertou! total de tentativas: {}'.format(contador))
