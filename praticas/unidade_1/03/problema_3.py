nome_1 = input('Nome: ')
idade_1 = int(input('Idade: '))

nome_2 = input('Nome: ')
idade_2 = int(input('Idade: '))

if idade_1 > idade_2:
    print(nome_1)
elif idade_1 < idade_2:
    print(nome_2)
else:
    print('Empate')