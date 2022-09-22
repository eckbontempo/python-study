n = input('Digite seu nome completo')

print('Seu nome: {}'.format(n.upper()))
print('Seu nome: {}'.format(n.lower()))

nsem = n.replace(' ','')
print('Quantidade de caracteres {}'.format(len(nsem)))

npri = n.split()
print('Quantidade de caracteres no primeiro nome {}'.format(len(npri[0])))