somaidade = 0
idademedia = 0
totalmulher = 0
nomevelho = 0
maioridade = 0

for c in range (1, 5):

    name = input('nome pessoa ', c )
    idade = int(input('nome pessoa ', c ))
    sexo = input('nome pessoa m/f ', c )
    somaidade += idade
    if c == 1 and sexo in 'm':
        maioridade = idade
        nomevelho = name
    if sexo in 'm' and idade > maioridade:
        maioridade = idade
        nomevelho = name
    if sexo in 'f' and idade < 20:
        totalmulher += 1
    
idademedia =  somaidade / 4

print('A media de didade do grupo é: ', idademedia)
print('Homem mais velho é {} tendo {} anos'.format(nomevelho, maioridade))
print('total de mulher com menos de 20 anos: ', totalmulher)
print(name)