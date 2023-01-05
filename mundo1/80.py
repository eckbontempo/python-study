num = list()

for c in range(0, 5):
    i = int(input("Digite o número: "))
    if c == 0 or i > num[-1]:
        num.append(i)
    else:
        pos = 0
        while pos < len(num):
             if i <= num[pos]:
                num.insert(pos, i)
                break

print(num)    
