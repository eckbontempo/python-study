ls = (int(input('Digite')),int(input('Digite')),int(input('Digite')),int(input('Digite')),int(input('Digite')))

print('Você digitou os números: ', end='')
for i in ls:
    print('{} '.format(i), end ='')

print('\nO valor 9 aparece {} vezes'.format(ls.count(9)))
if 3 in ls:
    print('o valor 3 apareceu pela primeira vez {}'.format(ls.index(3)+1))
else:  
    print('o valor 3 não foi digitado')
        
print('os valores pares digitados foram: ')
for c in ls:
    if c % 2 == 0:
        print('{} '.format(c), end='')

