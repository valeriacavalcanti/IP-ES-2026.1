numero = int(input('Número: '))
qtd = 1
maior = numero

while True:
    numero = int(input('Número: '))
    if numero > maior:
        maior = numero
    qtd += 1

    if qtd == 5:
        break

print(numero, maior)
