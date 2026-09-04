preco = float(input('Digite o preço do produto: '))

# Remove o '%' e converte para número
desconto = float(input('Digite o percentual de desconto: ').replace('%',''))

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print('Valor do desconto: R$ ' + str(round(valor_desconto,2)))
print('Preço final: R$ ' + str(round(preco_final,2)))

if preco_final < 50:
    print('Produto com preço baixo')
else:
    print('Produto com preço normal')