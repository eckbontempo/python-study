times = ('Corinthians','Palmeiras', 'Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense',
'Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória',
'Curitiba','Avaí','Ponte preta','Atlético-GO')

print('Os 5 primeiros colocados: ')
print(times[0:5])
print('Os 4 ultimos colocados: ')
print('{}'.format(times[16:]))
print('Times em ordem alfabetica: ')
print(sorted(times))

print('o Chapecoense  esta na possição: {}'. format(times.index('Chapecoense')+1))