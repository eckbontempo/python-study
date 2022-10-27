expr = str(input("Digite a expressão: "))

lista = list()

for s in expr:
    if s == '(':
        lista.append('(')
    elif s == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print("Express deu certo")
else:
    print("Express deu errado.")