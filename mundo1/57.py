sexo = str(input('Digite o sexo')).strip().upper()

while sexo not in 'MmFf':
    sexo = str(input('Erro, digite novamente'))