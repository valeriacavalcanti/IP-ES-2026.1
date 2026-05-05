# ler vários números inteiros, encerra quando for digitado 0 (zero).
# ao final, exiba TODOS os números que foram digitados.

numeros = []

while True:
    num = int(input('Número: '))
    if num == 0:
        break
    numeros.append(num)

print('eeeee')
print(numeros)
