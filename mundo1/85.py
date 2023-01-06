numeros, pares, impares = [], [], []

for c in range(0,6):
    
    num = int(input("Digite o número: "))
    if num % 2 == 0:
        pares.append(num)
        pares.sort()
    else:
        impares.append(num)
        impares.sort()

numeros.append(pares)
numeros.append(impares)

print("{}".format(numeros))