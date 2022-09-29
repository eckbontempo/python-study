
n1 = float(input('Digite reta 1'))
n2 = float(input('Digite reta 2'))
n3 = float(input('Digite reta 3'))

retas = sorted([n1 , n2 , n3])
soma = retas[0] + retas[1]

if soma >= retas[2]:
    print('Forma um triângulo')
    if retas[0] == retas[2] and retas [0] == retas[1]:
        print('do tipo equilátero')
    elif retas[0] == retas[1] and retas[0] != retas[2]:
        print('do tipo isósceles')
    elif retas[0] != retas[1] and retas[0] != retas[2]:
        print('do tipo escaleno')
else:
    print('Não forma um triângulo')
