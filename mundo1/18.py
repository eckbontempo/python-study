import math

n = float(input('Digite o angulo'))

#é necessário fazer a coversão de graus para radians
seno = math.sin(math.radians(n))
cos =  math.con(math.radians(n))
tan = math.tan(math.radians(n))

print('O cosseno é {} e o seno é {} e no tangente é o {}['.format(seno, cos, tan))
