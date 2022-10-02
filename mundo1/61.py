inicio = int(input('Digite o inicio'))
pa = int(input('Digite a PA'))
count = 0

while count != 10:
    print('{}'.format(inicio), end=' ')
    inicio = inicio + pa
    count += 1