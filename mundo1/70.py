total = qtdcaro = nomebarato = opc = cont = 0

while True:
    nome = input('nome do produto: ')
    preco = float(input('preço do produto'))
    cont +=1
    if cont == 1:
        menor = preco
    elif preco < menor:
        nomebarato = nome                  

    if preco > 1000:
        qtdcaro += 1
    
    opc = input('Deseja continua S/N')
    total += preco
    if opc in 'N':
        print('Programa finalizado')
        break
print(f'valor  total :{total}, produtosacima de 1000: {qtdcaro} produto mais barato: {nomebarato}')

