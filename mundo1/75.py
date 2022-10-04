n = (int(input('Digite o valor')),int(input('Digite o valor')),int(input('Digite o valor')),int(input('Digite o valor')))
pares = ()


print('o número 9 apareceu {}'.format(n.count(9)))
if 3 in n:
    print('o número 3 pareceu pela primeira vez {}'.format(n.index(3)+1))
else:
    print('o número 3 nao foi digitado')
print('Os valores parede digitados são:')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')