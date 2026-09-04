celsius = float(input('Digite a temperatura em celsius: '))

fahrenheit = (celsius * 9 / 5) + 32

print('A temperatura em fahrenheit é: ' + str(fahrenheit))

if celsius < 15:
    print('Frio')
elif celsius <= 30:
    print('Temperatura agradável')
else:
    print('Quente')