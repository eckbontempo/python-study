homemvelho = 0
maioridade = 0
idademedia = 0
idademulher = 0


for c in range(1,5):
    nome = str(input('nome da pessoa {}'.format(c)))
    idade = int(input('idade da pessoa {}'.format(c)))
    sexo = str(input('sexo e da pessoa m/f {}'.format(c)))
    idademedia += idade
    if c == 1 and sexo in 'm':
        homemvelho = nome
        maioridade = idade
    if sexo == 'm' and idade > maioridade:
        homemvelho = nome
        maioridade = idade
    if sexo == 'f' and idade < 20:
        idademulher += 1

print('Media da idade do grupo é {}'.format(idademedia / 4))
print('O nome do homem mais velho é {} e sua idade {}'.format(homemvelho, maioridade))
print('Total de mulher com menos de 20 anos: {}'.format(idademulher))