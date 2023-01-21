alunos = {}
todosalunos = []

while True:
    alunos['nome'] = input("Nome: ")
    if alunos['nome']  == "sair":
        break
    alunos['media']  = float(input("Media: "))

    if alunos['media']  >= 7:
        alunos['media']  = "aprovado"
    else:
        alunos['media']  = "reprovado"

    todosalunos.append(alunos.copy())

print("-"*30)
print(f"{'boleteim':^28}")
print("-"*30)

print(todosalunos)

for r in todosalunos:
    for k, v in r.items():
        print(f"{k}: ", end='')
        print(f"{v}", end='')
    print()
        