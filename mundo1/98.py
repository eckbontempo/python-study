import time

def printNum(a, b, c):
    if c == 0:
        print(f'contando de {a} até {b} em {1} em {1}: ')
    else:
        print(f'contando de {a} até {b} em {c} em {c}: ')

def contador(a, b, c):
    print(f'contando de {a} até {b} em {c} em {c}: ')

    if a < b and c != 0:
        while a <= b:
            print(f'{a} ', end='', flush=True)
            time.sleep(0.5)
            a += c
        print('FIM!')
    elif a < b and c == 0:
        c = 1
        while a <= b:
            print(f'{a} ', end='', flush=True)
            time.sleep(0.5)
            a += c
        print('FIM!')
    elif b < a and c != 0:
        while a >= b:
            print(f'{a} ', end='', flush=True)
            time.sleep(0.5)
            a -= c
        print('FIM!')
    elif b < a and c == 0:
        c = 1
        while a >= b:
            print(f'{a} ', end='', flush=True)
            time.sleep(0.5)
            a -= c
        print('FIM!')

contador(1, 10, 0)
contador(10, 0, 0)

print("agora chegou a sua vez de personalizar a contagem: ")
a = int(input("Inicio: "))
b = int(input("Fim: "))
c = int(input("Contador: "))

contador(a, b, c)
