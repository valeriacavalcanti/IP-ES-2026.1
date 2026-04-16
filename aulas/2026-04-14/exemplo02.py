'''
programa para ler vários números positivo. Calcular e exibir:
- média dos números lidos
- maior valor lido

O programa deverá encerrar quando for informado o valor 0 (zero).
'''

soma = 0
qtd = 0
maior = -1

num = int(input('Número: '))
while num != 0:    
    if num > maior:
        maior = num
    soma += num
    qtd += 1
    num = int(input('Número: '))

if qtd > 0:
    media = soma / qtd
    print(f'{media = }')
    print(f'{maior = }')
else:
    print('Erro')
