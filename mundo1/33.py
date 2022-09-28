import nturl2path


n1 = int(input('Digite o numero 1 '))
n2 = int(input('Digite o numero 2 '))
n3 = int(input('Digite o numero 3 '))

if n1 > n2:
    if n1 > n3:
        print('o numero {} é o maior'.format(n1))
    else:
        print('o numero {} é o maior'.format(n3))
else:
    if n2 > n3:
        print('o numero {} é o maior'.format(n2))
    else:
        print('o numero {} é o maior'.format(n3))

if n1 < n2:
    if n1 < n3:
        print('o numero {} é o menor'.format(n1))
    else:
        print('o numero {} é o menor'.format(n3))
else:
    if n2 < n3:
        print('o numero {} é o menor'.format(n2))
    else:
        print('o numero {} é o menor'.format(n3))

    