n = input('Digite uma frase')

tam = len(n)
acount = n.count('A')


print('Letras A encontradas {}, aparece pela primera vez na posição {}'.format(acount, n.find('A'), n.rfind('A')))
