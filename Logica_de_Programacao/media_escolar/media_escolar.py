nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))
nota_3 = float(input('Nota 3: '))

media = (nota_1 + nota_2 + nota_3) / 3
media = round(media, 2)
print('Media final: ' + str(media))

if media >= 10:
    print('Resultado: Aprovado')
elif media >= 5:
    print('Resultado: Recuperação')
else:
    print('Resultado: Reprovado')