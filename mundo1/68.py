from locale import windows_locale
import random
win = 0
escolha = ('impar', 'par')

while True:
    p2 = random.choice(escolha)
    p2n = random.randint(1, 5)
    print('Maquina escolheu {} e o número {}'.format(p2, p2n))
    if p2 == 'par':
        print('Foi escolhido o impar para você')
        p1 = 'impar'
    else:
        print('Foi escolhido o par para você')
        p1 = 'par'
    p1n = int(input('Agora escolha um número'))
    game = (p1n + p2n)%2
    if game == 0:
        if p1 == 'par':
            win += 1
            print('Você venceu, com seguência de wins: {}'.format(win))
        else:
            win = 0
            print('Você perdeu')
            break
    else:
        if p1 == 'impar':
            win += 1
            print('Você venceu, com seguência de wins: {}'.format(win))
        else:
            win = 0
            print('Você perdeu')
            break

print(p2)
print(p2n)

