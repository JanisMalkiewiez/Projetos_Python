# Solicita as informações ao usuário
numero = int(input("Digite qual número você quer ver a tabuada (ex: 5): "))
operador = input("Escolha um operador (+, -, *, /): ")

print(f'\n--- Tabuada do {numero} ---')

# Verifica se o operador é válido antes de iniciar o loop
if operador in ['+', '-', '*', '/']:
    for i in range(1, 11):
        if operador == '+':
            print(f'{numero} + {i} = {numero + i}')
        elif operador == '-':
            print(f'{numero} - {i} = {numero - i}')
        elif operador == '*':
            print(f'{numero} x {i} = {numero * i}')
        elif operador == '/':
            # Formata a divisão para exibir apenas 2 casas decimais
            print(f'{numero} / {i} = {numero / i:.2f}')
else:
    print("Operador inválido! Por favor, execute o programa novamente e escolha +, -, * ou /.")