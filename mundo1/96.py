def area(a, b):
    result = a * b
    return result


def pergunta():
    a = float(input("Largura: "))
    b = float(input("Altura: "))
    return a, b

print('-'*25)
print(f"{'cálculo da árae':^30}")
print('-'*25)

a, b = pergunta()
result = area(a, b)

print(f'a área de um terreno {a}x{b} é de {result}m')