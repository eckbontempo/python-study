import random

lista = []

qtd = int(input("Quantos jogos? "))

for indice in range (0, qtd):
    jogo = []
    for c in range (0, 6):
        n = random.randint(1, 60)
        while True:
            if len(jogo) == 0 or n not in jogo:
                jogo.append(n)
                break
            elif n in jogo:
                n = random.randint(1, 60)
    lista.append(jogo)
    
for n in range(0, len(lista)):
    print(lista[n])
           

