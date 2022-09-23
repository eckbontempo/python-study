n = float(input('Digite o KM da viagem'))

if n < 200:
    print('Valor a pagar para viagens curtas R${}'.format(n*0.50))
else:
    print('Valor a pagar para viagens longas R${}'.format(n*0.45))