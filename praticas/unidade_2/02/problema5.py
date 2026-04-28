for i in range(2):
    print('Rodada:', i)
    soma_amarelo = 0
    soma_vermelho = 0
    for j in range(2):
        print('Jogo:', j)
        amarelo = int(input('Cartões amarelos: '))
        vermelho = int(input('Cartões vermelhos: '))

        soma_amarelo += amarelo
        soma_vermelho += vermelho
    print(f'Rodada: i')
    print(f'{soma_amarelo = }')
    print(f'{soma_vermelho = }')
