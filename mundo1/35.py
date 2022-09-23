l1 = float(input('Digite o valor da reta 1 '))
l2 = float(input('Digite o valor da reta 1 '))
l3 = float(input('Digite o valor da reta 1 '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode formar um triangulo')
else:
    print('Não forma um triangulo')