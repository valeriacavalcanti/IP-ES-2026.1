media_semestral = int(input('Média semestral: '))
avaliacao_final = int(input('Avaliação Final: '))

media_final = ((media_semestral * 6) + (avaliacao_final * 4))/10

print(f'Média Final: {media_final:.0f}')