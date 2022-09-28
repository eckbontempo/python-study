n =  int(input('Digite um numero'))

x = int(input('1 - Bin\n 2 - Octal\n 3 - Hex\n '))

if x == 1:
    print(bin(n)[2:])
elif x == 2:
    print(oct(n)[2:])
elif x == 3:
    print(hex(n)[2:])