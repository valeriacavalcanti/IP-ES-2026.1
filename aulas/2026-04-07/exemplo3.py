'''
Ler uma nota válida para o Suap.
'''

nota = int(input('Nota: '))

while nota < 0 or nota > 100:
    print('nota inválida')
    nota = int(input('Nota: '))

print(f'{nota = }')
