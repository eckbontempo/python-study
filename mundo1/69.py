conthomem = contmulher = opc =  mais18 = 0


while True:

    idade = int(input('Idade: '))
    sexo = input('Sexo: ')

    if idade > 18:
        mais18 += 1

    if sexo in 'M':
        conthomem += 1

    if sexo in 'F':
        if idade < 20:
            contmulher += 1
           
    print('conthomem {} contmulher {} e mais 18 {}'.format(conthomem, contmulher, mais18))

    opc = input('Quer continuar S/N? ')
    if opc == 'N':
        print('Programa finalizado')
        break
