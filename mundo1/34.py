n = float(input('Digite o salário'))

if n >= 1250:
    print('O aumento do salário será de: R${}'.format(0.1*n + n))
else:
    print('O aumento + do salário será de: R${}'.format(0.15*n + n))