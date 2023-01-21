jogador = {}
gols = []

jogador['nome'] = input('nome: ')
qtd_jogos = int(input('qtd de jogos: '))
for c in range (0, qtd_jogos):
    gols.append(int(input('gols: ')))   
jogador['gols'] = gols
jogador['total_gols'] = sum(jogador['gols'])

print('O jogador {} o jogou o total de: {}'.format(jogador['nome'], len(jogador['gols'])))
for c in range(0, len(jogador['gols'])):
    print('na partida {}'.format(c), end='')
    print(', fez {} gols'.format(jogador['gols'][c]))