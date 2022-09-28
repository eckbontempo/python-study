from datetime import date

data = date.today().year

#n = int(input('Digite o ano que você nasceu: '))

n2 = 21
# n2 = data - n

if n2 <= 9:
    print(' CATEGORIA MIRIM')
elif n2 <= 14 and n2 > 9:
    print('CATEGOARIA INFANTIL')
elif n2 <= 19 and n2 >14:
    print('CATEGORIA JUNIOR')
elif n2 <= 20:
    print('CATEGOARIA SÊNIOR')
elif n2 > 20:
    print('CATEGORIA MASTER')