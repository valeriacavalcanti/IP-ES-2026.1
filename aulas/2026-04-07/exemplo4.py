'''
Ler uma nota válida para o Suap.
'''

while True:
    nota = int(input('Nota: '))

    if nota >= 0 and nota <= 100:
        break

    print('nota inválida')


print(f'{nota = }')
