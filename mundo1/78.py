numero = []

for c in range(0,5):
    c = int(input("Digite o valor"))
    numero.append(c)

numero.sort()

print('o maior número é {}, e o menor é {}'.format(numero[4], numero[0]))