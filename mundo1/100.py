import random

def randomnum():
    lista = []
    for c in range(0, 5):
        lista.append(random.randint(0, 10))
    return lista

def soma_par(* num):
    total = 0
    for valor in num:
        for c in valor:
            if c % 2 == 0:
                total += c
    print(f'foi gerado a lista de numeros: {valor} e a soma de todos os números pares é: {total}')
    
listaa = randomnum()
soma_par(listaa)