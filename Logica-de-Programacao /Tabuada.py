# Fazer as tabuadas de 1 até 10

for i in range(10):
    print(f'Tabuada do {i+1}')
    for j in range(10):
        print(f'{i + 1} x {j + 1} = {(i+1) * (j+1)}')
