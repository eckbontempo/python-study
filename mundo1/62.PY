num = int(input('Digite o Primeiro Termo da PA: '))
termos = 10
razão = int(input('Digite a Razão da PA: '))
cont = 1

while cont <= termos:
    print(f'{num}', end=' ')
    num += razão
    cont += 1
    if cont == termos + 1:
        termos = int(input('\nQuantos Termos a mais da PA você deseja ver: '))
        cont = 1
