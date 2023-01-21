import random

game = [{'jogadores1': random.randrange(1, 6)},
        {'jogadores2': random.randrange(1, 6)},
        {'jogadores3': random.randrange(1, 6)},
        {'jogadores4': random.randrange(1, 6)}]

sort_jogadores = []

while len(game) != 0:
    maior_jogo = {}
    for r in game:
        for k, v in r.items():
            if len(maior_jogo) == 0:
                maior_jogo[k] = v
                maior_numero = v
            elif maior_numero <= v:
                maior_jogo = {}
                maior_jogo[k] = v
                maior_numero = v

    sort_jogadores.append(maior_jogo.copy())
    for exclui in game:
        if maior_jogo == exclui:
            game.remove(exclui)

print("-"*30)
print(f"{'RANKING':^28}")
print("-"*30)
for c in sort_jogadores:
    for k, v in c.items():
        print(f"O {k} tirou {v}")

# from random import randint
# import operator

# jogo = {'jogador1': randint(1, 6),
#         'jogador2': randint(1, 6),
#         'jogador3': randint(1, 6),
#         'jogador4': randint(1, 6)}
# ranking = {}
# for k, v in jogo.items():
#     print(f" o {k} tirou {v} no dado")

# ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
# print(ranking)