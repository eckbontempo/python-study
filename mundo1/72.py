num = ('zero','um','dois','três', 'quatro','cinco','seis', 'sete', 'oito','nove', 'dez', 'onze', 'doze','treze','quatorze','quinze','dezesseis','dezessete', 'dezoito','dezenove','vinte')

n1 = int(input('Digite o número entre 0 e 20: '))
while True:
    if n1 >= 0 and n1 <=20:
        print('Você digitou o {}'.format(num[n1]))
        break
    else:
        n1 = int(input('Erro! Digite novamente número entre 0 e 20: '))
