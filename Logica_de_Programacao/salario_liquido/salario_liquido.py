salario_bruto = float(input('Digite o valor do salário: '))
descontos = float(input('Digite o valor do desconto: '))

salario_liquido = salario_bruto - descontos

print('O salário líquido é: R$ ' + str(round(salario_liquido,2)))


if salario_liquido < 1500:
    print('Salário líquido baixo.')
elif salario_liquido <= 3000:
    print('Salário líquido médio.')
else:
    print('Salário líquido alto.')