from operator import invert


text = str(input('Digite a frase: ')).replace(' ', '')

textinver = text[::-1]

if textinver == text:
    print('A frase é um palíndro')
else:
    print('Não é um palíndro')
    
    