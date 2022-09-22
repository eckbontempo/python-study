n = input('Digite o nome da cidade')

sep = n.split()

print('A cidade digitada começa com a palavra SANTO: {}'.format((sep[0] in 'SANTO')))