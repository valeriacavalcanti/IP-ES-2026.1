# programa para ler 10 números inteiros.

soma = 0
#numeros = [0,0,0,0,0,0,0,0,0,0]
numeros = [0] * 4

for i in range(len(numeros)):
    numeros[i] = int(input('Número: '))
    soma += numeros[i]
    #print(numeros)

media = soma / len(numeros)

# verificar quantos numeros lidos possuem valor acima da média
qtd = 0
for i in range(len(numeros)):
    if numeros[i] > media:
        qtd += 1
        
print(f'{media = }')
print(f'{qtd = }')

for i in range(len(numeros)):
    if numeros[i] < media:
        print(numeros[i])
        
