conthomem = contmulher = opc =  mais18 = 0


while True:

    idade = int(input('Idade: '))
    sexo = input('Sexo: ')

    if sexo in 'M':
        conthomem += 1
    elif sexo in 'F':
        if idade < 20:
            contmulher += 1
    
    if idade > 18:
        mais18 += 1

    print()


    opc = input('Quer continuar S/N? ')
    if opc == 'N':
        print('Programa finalizado')
        break
