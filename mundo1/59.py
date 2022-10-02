n1 = int(input('Digite o valor do número'))
n2 = int(input('Digite o valor do número'))

opc = int(input('Escolhe as opções abaixo:'))

while  opc != 0:

    

    if opc == 1:
        print('Soma: {} + {} = {}'.format(n1,n2,n1+n2))

    if opc == 2:
        print('Multiplicação: {} * {} = {}'.format(n1,n2,n1*n2))

    if opc == 3:

        if n1 > n2:
            print('O número {} é maior que o {}'.format(n1,n2))
        else:
            print('O número {} é maior que o {}'.format(n2,n1))

    if opc == 4:
        print('Novos números!')
        n1 = int(input('Digite o valor do número'))
        n2 = int(input('Digite o valor do número'))

    if opc == 5:
        break
    
    opc = int(input('Escolhe as opções abaixo:'))