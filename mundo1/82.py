lista = list()
pares = list()
impares = list()

while True:
    lista.append(int(input("digite o valor")))
    if 00 in lista:
        break

for c in range(len(lista)):
    if c%2 == 0:
        if c != 0:
            pares.append(c)
    elif c%2 != 0:
        impares.append(c)

print(f'lista completa : {lista}')
print(f'pares : {pares}')
print(f'impares : {impares}')
