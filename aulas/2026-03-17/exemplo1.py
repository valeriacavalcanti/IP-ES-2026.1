# programa para ler um valor e conceder aumento de 10%

valor = float(input('Digite um valor: '))

if (valor >= 0):
    aumento = valor * 0.1
    valor = valor + aumento

    print(f'{valor=}')
else:
    print('Valor inválido')
