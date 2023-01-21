import datetime

now = datetime.datetime.now()
year = now.year

pessoa = {}

while True:
    pessoa['nome'] = input("nome: ")
    pessoa['nascimento'] = year - int(input("ano de nascimento: "))
    pessoa['ctps'] = int(input("ctps: "))
    if pessoa['ctps'] == 0:
        print("achei um desemepregado")
        break
    else:
        pessoa['ano_contratacao'] = int(input('ano da contratação: '))
        pessoa['salario'] = float(input('salario: '))
        pessoa['aposentadoria'] =  (35 - (year - pessoa['ano_contratacao'])) + pessoa['nascimento']
        break
print(pessoa)






