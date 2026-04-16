'''
Programa para ler do usuário a quantidade de números.
Ler os (n) valores.
Ao final, informar o maior valor digitado.
'''

qtd = int(input('Quantidade: '))

for i in range(qtd):
    num = int(input('Número: '))

    if i == 0:
        maior = num
    else:
        if num > maior:
            maior = num

print(maior)
