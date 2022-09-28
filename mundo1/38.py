n1 = float(input('Digite o valor 1 '))
n2 = float(input('Digite o valor 2 '))

if n1 < n2:
    print('{} é maior que o {}'.format(n1, n2))
elif n1 > n2:
    print('{} é maior que o {}'.format(n2, n1))
else:
    print('Não existe os valores são iguais')