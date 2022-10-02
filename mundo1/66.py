contar = soma = 0
while True:
    n = int(input('digite o número - aperta[999] para parar.'))
    if n == 999:
        break
    else:
        contar += 1
        soma += n
print(f'total de números digitados: {contar} e a soma entre eles: {soma}')
    


