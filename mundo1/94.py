dados = {}
pessoas, todas_mulheres, acima_media =[], [], []


while True:
    dados['nome'] = input('nome: ')
    if dados['nome'] == 'sair':
        break
    dados['sexo'] = input('sexo: ')
    dados['idade'] = int(input('idade: '))
    media_idade =+ dados['idade']
    pessoas.append(dados.copy())
    dados.clear

print('quantidade de pessoas cadastradas: {}'.format(len(pessoas)))
print('media de idade das pessoas cadastradas é: {}'.format(media_idade))
for c in pessoas:
    if c['sexo'] == 'f':
        todas_mulheres.append(c)
    
    if c['idade'] > media_idade:
        acima_media.append(c)
print('todas as mulheres cadastradas: {}'.format(todas_mulheres))
print('pessoas acima da media de idade: {}'.format(acima_media))