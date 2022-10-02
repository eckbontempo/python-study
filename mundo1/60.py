
numero = int(input('Digite o valor para ser fatorado.'))
count = numero
soma = numero

while count != 1:
    count -= 1
    soma = soma * count
    
print(soma)

#n = 0 #numero
#c = n #contador
#f = 1 #base fatorial
#print('Calculando {}! = '.format(n), end='')
#while c > 0:
#    print('{}'.format(n), end='')
#    print(' x ' if c > 1 else ' = ',  end='')
#    f *=c
#    c -= 1
#print('{}'.format(f))

