while True:
    n = int(input('quer ver a tabuada de qual valor?'))
    #fecha
    if n <= -1:
        break
    for cont in range(1 , 10):
        print('{} x {} = {}'.format(n, cont + 1, (cont+1)*2))