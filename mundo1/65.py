
soma = cont = qtd = media = maiorn = menorn = 0
opc = 's'

while opc not in 'N':
    n = int(input('Digite o número '))
    soma += n
    cont += 1
    qtd += 1

    if qtd == 1:
        maiorn = menorn = n
    else:
        if n > maiorn:
            maiorn = n
            print(maiorn)

        if n < menorn:
            menorn = n
            print(menorn)
    opc = input('Quer continuar S/N')
media = soma / qtd    
print('Qtd: {},  média: {}, soma: {}, maior: {}, menor: {} '.format(qtd, media, soma, maiorn, menorn))
