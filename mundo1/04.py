from re import A


n = input('Digite algo')

print('O que foi digitado é numero:', type(n))
print('O que foi digitado tem espaço:', n.isspace())
print('O que foi digitado é MAIúCUSCULO :', n.isupper()) 
print('O que foi digitado é MINÚSCULO :', n.islower())
print('O que foi digitado é numero:', n.isnumeric())
print('O que foi digitado é letra:', n.isalpha())