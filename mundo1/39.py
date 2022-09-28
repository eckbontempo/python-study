from datetime import date

today = date.today().year
ano = int(input('Digite o ano de nascimento'))
alist = today - ano

if alist > 18:
    print('Você já deveria estar alistado a {} anos'.format(alist - 18))
elif alist == 18:
    print('Você deverá se alistar esse ano')
else:
    print('Você deverá se alistar em {}'.format((18 - alist) + today))



