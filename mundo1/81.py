lista = list()

while True:
    n = int(input("Digite o valor: "))
    lista.append(n)
    resp = input("Deseja continuar S/N")
    if resp in "nN":
        break

print(f'total de número digitados {len(lista)}')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('encontrei o 5')
else:
    print('Não encontrei o 5')