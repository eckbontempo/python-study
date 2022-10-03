n1 = n10 = n20 = n50 = 0

saldo = int(input('Digite o valor do saque'))

while True:

    if saldo >= 50:
        saldo = saldo - 50 
        n50 += 1
    elif saldo >= 20:
        saldo = saldo - 20
        n20 += 1
    elif saldo >= 10:
        saldo = saldo - 10
        n10 += 1
    elif saldo >= 1:
        saldo = saldo - 1
        n1 += 1
    elif saldo == 0:
        break
    

print(f'Notas de 50 {n50}, notas de 20 {n20}, notas de 10 {n10} e notas de 1 {n1}')
