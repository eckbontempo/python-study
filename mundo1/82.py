lista, listapares, listaimpares = list(), list(), list()

num = int(input("Digite o valor"))
while True:
    if num == 999:
        print(f"lista: \n{lista}")
        print(f"lista de pares: \n{listapares}")
        print(f"lista de impares: \n{listaimpares}")
        break
    else:
        lista.append(num)
        if num % 2 == 0:
            listapares.append(num)
        else:
            listaimpares.append(num)
    num = int(input("Digite o valor"))

