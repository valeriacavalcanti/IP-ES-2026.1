qtd_aulas = int(input('Quantidade de aulas: '))
qtd_faltas = int(input('Quantidade de faltas: '))

qtd_presenca = qtd_aulas - qtd_faltas

frequencia = qtd_presenca/qtd_aulas * 100

print(f'Frequência: {frequencia:.1f}%')