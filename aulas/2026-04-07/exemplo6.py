'''
Para ler vários número inteiros. O programa deverá encerrar quando
for informado o valor 0 (zero).

Ao final, exiba a quantidade de valores negativos e positivos que foram
digitados.
'''

qtd_pos = qtd_neg = 0

while True:
    valor = int(input('Valor: '))
    
    if valor == 0:
        break
    
    if valor > 0:
        qtd_pos = qtd_pos + 1
    else:
        qtd_neg = qtd_neg + 1
        
    
print(f'{qtd_pos = }')
print(f'{qtd_neg = }')
