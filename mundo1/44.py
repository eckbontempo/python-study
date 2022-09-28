preco = float(input('Valor do produto: '))

x = int(input('Pagamento:\n 1 - Vista dinheiro/cheque\n 2 - Vista c/ cartão\n 3 - Pagamento em 2x\n 4 - Pagamento em 3x\n Digite a opção: '))

if x == 1:
    print('O valor a ser pago é R$:{:.2f}'.format(preco-(0.1*preco)))
elif x == 2:
    print('O valor a ser pago é R$:{:.2f}'.format(preco-(0.05*preco)))
elif x == 3:
    print('O valor a ser pago é R$:{:.2f}'.format(preco))
elif x == 4:
    print('O valor a ser pago é R$:{:.2f}'.format(preco + (0.2*preco)))
     
