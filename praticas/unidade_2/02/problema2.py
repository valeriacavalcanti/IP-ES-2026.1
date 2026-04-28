QTD = 4
soma = 0
aprovado = final = reprovado = 0

for i in range(QTD):
    nota = int(input('Nota: '))

    if nota >= 70:
        aprovado += 1
    elif nota >= 40:
        final += 1
    else:
        reprovado += 1

    soma += nota

media = soma / QTD

print(f'{media = }')
print(f'{aprovado = }')
print(f'{final = }')
print(f'{reprovado= }')
