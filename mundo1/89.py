lista = [['nome:'],['nota1:'],['nota2:'],['media:']]

while True:

    nome = input("Nome: ")
    if nome == "sair":
        break
    n1 = float(input("Nota: "))
    n2 = float(input("Nota 2: "))
    media = (n1+n2)/2

    lista[0].append(nome)
    lista[1].append(n1)
    lista[2].append(n2)
    lista[3].append(media)

print("-="*15)
print(f"{'BOLETIM':^25}")
print("-="*15)

for c in range(0, len(lista[0])):
    print(f"{lista[0][c]:>10} {lista[1][c]:>10} {lista[2][c]:>10} {lista[3][c]:>10}")    

print("-="*15)

alunoview = input("Digite o nome do aluno para ver a suas notas: ")
while True:
    if alunoview in lista[0]:
        c = lista[0].index(alunoview)
        print(f"{lista[0][c]:>10} {lista[1][c]:>10} {lista[2][c]:>10} {lista[3][c]:>10}")
        continua = input("Deseja visualizar outro aluno: ")
        if continua in 'sim':
            alunoview = input("Digite o nome do aluno para ver a suas notas: ")
        else:
            print("PROGRAMA FINALIZADO")
            break
    else:
        alunoview = input("Aluno não encontrado, digite o nome do aluno para ver a suas notas: ")
        if alunoview == 'sair':
            break


    
