numero = int(input('Número: '))
maior = numero

for i in range(4):
    numero = int(input('Número: '))
    if numero > maior:
        maior = numero

print(numero, maior)
