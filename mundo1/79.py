lista = list()

while True:
    num = int(input("Digite o valor"))
    if num == 999:
        print("programa finalizado")
        break
    else:
        if num not in lista:
            lista.append(num)

print(sorted(lista))