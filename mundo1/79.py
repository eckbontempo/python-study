from re import T


num = [0]

while True:

    c = int(input("Digite o valor"))

    if c not in num:
        num.append(c)
        print('numero cadastrado')
    
    r = input('seja continua S/N')
    if r in "Nn":
        break

num.sort()

print(num)

