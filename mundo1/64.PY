cont = 0
n2 = 0
n1 = 0
while n1 != 999:
    n1 = int(input('Digite o número'))
    if n1 != 999:
        n2 = n2 + n1
        cont += 1
print(' a soma: {} total de números digitados {}'.format(n2, cont))