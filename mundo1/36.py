casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
qts = float(input('Número de anos:'))

anos = qts * 12

parc = casa / anos

if parc <= (0.3 * salario):
    print('O valor da parcela é: R${} durante em {} anos'.format(parc, qts))
else:
    print('Empréstimo negado!!!')
