from problema3 import fraude, desconto_superior

qtd_fraude = qtd_desconto_superior = 0

qtd = int(input('Quantidade avaliadada: '))

for i in range(qtd):
    valor_antes = float(input('Valor antes: '))
    valor_depois = float(input('Valor depois: '))
    if fraude(valor_antes, valor_depois) == True:
        qtd_fraude += 1
    if desconto_superior(valor_antes, valor_depois) == True:
        qtd_desconto_superior += 1

print(f'{qtd_fraude = }')
print(f'{qtd_desconto_superior = }')
