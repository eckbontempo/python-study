
sexo = input('Digite o sexo').strip().upper()[0]

while sexo not in 'MF':
    sexo = input('Erro! Digite novamente ').strip().upper()[0]
print('Fim')
