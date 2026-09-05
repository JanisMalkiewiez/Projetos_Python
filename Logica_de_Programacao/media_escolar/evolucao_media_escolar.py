nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))
nota_3 = float(input('Digite a 3° nota: '))
nota_4 = float(input('Digite a 4° nota: '))

media = round((nota_1 + nota_2 + nota_3 + nota_4) / 4, 2)
print('Média final: ' + str(round(media, 2)))

# Verificação da Situação
if media >= 7:
    situacao = 'Aprovado'
elif media >= 5:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

# Verificação do Desempenho
if media >= 9:
    desempenho = 'Excelente desempenho'
elif media >= 7:
    desempenho = 'Bom desempenho'
elif media >= 5:
    desempenho = 'Precisa melhorar'
else:
    desempenho = 'Estude mais os fundamentos'

# Exibindo os resultados finais
print('Status: ' + situacao)
print('Feedback: ' + desempenho)
