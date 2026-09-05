valor_pago = float(input('Valor pago:'))
valor_investido = float(input('Valor investido:'))
valor_venda = float(input('Valor da venda:'))

custo_total = valor_pago + valor_investido
lucro = valor_venda - custo_total

print('Custo total:R$ ' + str(round(custo_total, 2)))
print('Lucro/Prejuízo:R$ ' + str(round(lucro, 2)))

if lucro > 0:
    comissao = lucro * 5 / 100
else:
    comissao = 0

print('Comissão do vendedor:R$ ' + str(round(comissao, 2)))

if lucro > 5000:
    print('Resultado: Venda muito lucrativa!')
elif lucro > 0:
    print('Resultado: Venda lucrativa!')
elif lucro == 0:
    print('Resultado: Venda empatada!')
else:
    print('Resultado: Venda com prejuízo!')
