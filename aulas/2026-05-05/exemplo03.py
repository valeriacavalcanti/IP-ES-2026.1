# ler 4 valores e DEPOIS exibir os valores digitados

numeros = [0] * 4

for i in range(4):
    numeros[i] = int(input('Valor: '))

# exibir os valores digitados
for i in range(4):
    print(i, numeros[i])

# exibir os valores digitados
for num in numeros:
    print(num)
