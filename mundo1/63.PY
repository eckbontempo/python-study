termo = int(input('digite a qtd de termos '))
n1 = 0
n2 = 1
cont = 3
print('{} -> {}'.format(n1,n2), end='')
while cont <= termo:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
    print(' -> {}'.format(n3), end='')
