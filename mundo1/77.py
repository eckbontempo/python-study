palavra = ('beringela', 'dado', 'fogo', 'amor', 'vogal', 'computador', 'piramide')

for p in palavra:
    print(f'\n{p} possui:')
    for l in p:
        if l in 'aeiou':
            print(f'{l} ', end='')