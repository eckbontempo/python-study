n = float(input('Quantos dias utilizado'))
y = float(input('Quantos KM percorridos'))

vn = 60 * n
vy = 0.15 * y 

print('O valor total das diarias: \n dias{:3.0f} valor: R${:.2f}'.format(n, vn))
print('O valor total por KM rodado valor: R${:.2f}'.format(vy))
print('total: R${}'.format(vy+vn))