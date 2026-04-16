'''
Programa para ler 6 números. Exibir a média e o maior.
'''

soma = 0
for i in range(6):
    num = int(input('Número: '))
    soma = soma + num

media = soma / (i + 1)

print(f'{media}')
