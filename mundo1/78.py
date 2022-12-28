lista = list()

for c in range(0, 5):
    lista.append(int(input("Digite o valor {} ".format(c))))

mai = lista[0]
indexmai = 0
men = lista[0]
indexmen = 0

for c, v in enumerate(lista):
    if v > mai:
        main = v
        indexmai = c

    if v < men:
        men = v
        index = c


print("o valor maior é {} e esta na posicao {}".format(main, indexmai))
print("o valor menor é {} e esta na posicao {}".format(men, indexmen))