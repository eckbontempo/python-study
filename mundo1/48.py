s = 0
x = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        x += 1
    
print('no total são: {} e a soma de todos os números é: {}'.format(x,s))