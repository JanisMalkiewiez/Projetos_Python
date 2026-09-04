distancia = float(input('Digite a distância percorrida: '))
consumo = float(input('Digite o consumo médio do carro em km/l:  '))
preco_combustivel = float(input('Digite o preço do combustível: '))

litros_necessarios = distancia / consumo
custo_viagem = litros_necessarios * preco_combustivel

print('A distância percorrida foi: ' + str(round(distancia, 2)) + ' km')
print('Litros necessários: ' + str(round(litros_necessarios, 2)) + ' litros')
print('Custo total: R$: ' + str(round(custo_viagem, 2)))

if custo_viagem < 100:
    print('Viagem econômica')
elif custo_viagem <= 300:
    print('Custo moderado')
else:
    print('Viagem cara')