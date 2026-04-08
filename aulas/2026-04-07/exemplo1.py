# quero um valor POSITIVO

num = int(input('Número positivo: '))

while num <= 0:
    print('Número inválido')
    num = int(input('Número positivo: '))

print(f'{num = }')
