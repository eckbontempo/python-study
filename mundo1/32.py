n = int(input('Digite o ano'))

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('o anoe é bissexto')
else:
    print('o ano não é bissexto')