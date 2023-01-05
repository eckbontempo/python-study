pessoas = []

while True:
    nome = input("Nome: ")
    if nome == "sair":
        break
    peso = int(input("Peso: "))
    if peso == "00":
        break
    pessoas.append([nome, peso])

def compara_peso(pes1):
    return pes1[1]

pessados = sorted(pessoas, key=compara_peso)

leve = sorted(pessoas,reverse=True, key=compara_peso)

print(f"Lista de mais pessados {pessados}")
print(f"Lista de mais leves {leve}")
print(f"Total de registro {len(pessoas)}")





    
