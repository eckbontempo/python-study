matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somater = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input("digite o valor: "))
    
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

for l in range(0, 3):
    somater += matriz[l][2]
    
maior = matriz[0][1]
for c in range(0, 3):
    if maior < matriz[c][1]:
        maior = matriz[c][1]

print(f"a soma dos números pares é {soma}")
print(f"a soma dos números terceira coluna é {somater}")
print(f"maior numero da segunda coluna {maior}")                 