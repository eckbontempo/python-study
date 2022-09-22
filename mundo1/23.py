n = int(input('Digite um número'))

uni = n // 1 % 10
dez = n // 10 % 10
cent = n // 100 % 10
mil = n // 1000 % 10

print('Unidades: {}'.format(uni))
print('Dezenas: {}'.format(dez))
print('Centenas: {}'.format(cent))
print('Milha: {}'.format(mil))