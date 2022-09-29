from datetime import date

data = date.today().year

maior = 0
menor = 0

for pess in range (1,8):
    nasc = int(input('Digite o ano de nascimento da pessoa '))
    idade = data - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Pessoas com mais de 18 anos: {}, com menos de 18 anos: {}'.format(maior, menor))