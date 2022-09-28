import random

player1 = ['Pedra' , 'Papel', 'Tesoura']
p1 = random.choice(player1)

p2 = input('Digite sua escolha: ')

if p2 == p1:
    print('Empate')
elif p2 ==  'Pedra' != p1 and p1 != 'Papel':
    print('Ganhou!!! {} ganha de {}'.format(p2, p1))
elif p2 ==  'Pedra' != p1:
    print('Perdeu!!! {} ganha de {}'.format(p1, p2))
elif p2 ==  'Tesoura' != p1 and p1 != 'Pedra':
    print('Ganhou!!! {} ganha de {}'.format(p2, p1))
elif p2 ==  'Tesoura' != p1:
    print('Perdeu!!! {} ganha de {}'.format(p1, p2))
elif p2 ==  'Papel' != p1 and p1 != 'Tesoura':
    print('Ganhou!!! {} ganha de {}'.format(p2, p1))
elif p2 ==  'Papel' != p1:
    print('Perdeu!!! {} ganha de {}'.format(p1, p2))

