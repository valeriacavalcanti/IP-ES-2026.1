''''
num = 0

while True:
    print('A - Aumentar')
    print('D - Diminuir')
    print('S - Sair')

    codigo = input('Informe o código: ')

    if codigo == 'A':
        num += 1
    elif codigo == 'D':
        num -= 1
    elif codigo == 'S':
        break
    else:
        print('Código inválido')

print('Valor final:', num)
'''

num = 0

print('A - Aumentar')
print('D - Diminuir')
print('S - Sair')

codigo = input('Informe o código: ')

while codigo != 'S':
    if codigo == 'A':
        num += 1
    elif codigo == 'D':
        num -= 1
    else:
        print('Código inválido')
    
    print('A - Aumentar')
    print('D - Diminuir')
    print('S - Sair')

    codigo = input('Informe o código: ')

print('Valor final:', num)