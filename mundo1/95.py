
jogador = {}
todos_jogadores, gols = [], []

while True:
    gols.clear()
    jogador.clear()
    jogador['nome'] = input('nome: ')
    if jogador['nome'] == 'sair':
        break
    jogador['partida'] = int(input('quantas partidas: '))
    for c in range(1, jogador['partida'] + 1):
        gols.append(int(input('quantos gols o jogador fez na partidade {}: '.format(c))))
    jogador['gol'] = gols[:]
    jogador['total'] = sum(gols)
    todos_jogadores.append(jogador.copy())

print('-='*30)
print('cod ', end='')
for chaves in todos_jogadores[0].keys():
    print(f'{chaves:<15}', end='')
print()
for k, v in enumerate(todos_jogadores):
    print(f'{k:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<13}', end='')
    print()
print('-='*30)
seleciona_jogador = int(input('Digite o código do jogador que deseja vizualizar: '))
while True:
    if seleciona_jogador == 99:
        break
    elif seleciona_jogador <= len(todos_jogadores):
        print('-='*30)
        print('cod ', end='')
        for chaves in todos_jogadores[0].keys():
            print(f'{chaves:<15}', end='')
        print()
        for valor in todos_jogadores[int(seleciona_jogador)].values():
            print(f'{str(valor):<13}', end='')
        print()
        print('-='*30)        
        seleciona_jogador = int(input('Digite o código de outro jogador que deseja vizualizar: '))
    else:
        seleciona_jogador = int(input('Jogador não encontrado, digite o código do jogador que deseja vizualizar: '))