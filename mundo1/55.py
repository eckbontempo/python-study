pmaior = 0

for c in range (1, 4):
    pessoas = float(input('Peso da pessoa {}'.format(c)))
    pmenor = pessoas

    if pessoas > pmaior:
        pmaior = pessoas
    
    if pessoas < pmenor:
        pmenor = pessoas

print('Maior pesso: {} e menor peso: {} '.format(pmaior, pmenor))


