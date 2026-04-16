'''
Programa para ler do usuário a quantidade de números.
Ler os (n) valores.
Ao final, informar o maior valor digitado.
'''

qtd = int(input('Quantidade: '))

if qtd == 0:
    print('ok')
else:
    maior = int(input('Número: '))

    for i in range(qtd - 1):
        num = int(input('Número: '))

        if num > maior:
            maior = num

    print(maior)
