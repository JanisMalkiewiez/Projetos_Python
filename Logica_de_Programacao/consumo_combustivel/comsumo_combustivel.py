distancia = float(input('Digite a distância percorrida: '))
litros = float(input('Digite quantos litros foram consumidos: '))

consumo = distancia / litros

print('Consumo do combustível: ' + str(round(consumo, 2)) + ' km/l')

if consumo < 8:
    print('Consumo alto!')
elif consumo <= 12:
    print('Consumo médio!')
else:
    print('Consumo baixo!')