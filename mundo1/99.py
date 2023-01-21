def maior(* a):
    tam = len(a)
    maior_num = None
    for valor in a:
        if not maior_num:
            maior_num = valor
        elif maior_num < valor:
            maior_num = valor
    print(f'os valores digitados são {a}, com o total de {tam} números, e o maior número encontrado foi {maior_num}')

maior(1, 8, 3, 4)
