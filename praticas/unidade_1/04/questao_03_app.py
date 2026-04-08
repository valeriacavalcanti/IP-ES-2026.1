from questao_03_funcoes import *

## Código Principal

valor_unitario = float(input('Informe o valor unitário (em dólar): '))
qtd = int(input('Informe a quantidade comprada: '))

valor_compra_dolar = calcular_valor_compra(valor_unitario, qtd)
valor_compra_real = converter_dolar_para_real(valor_compra_dolar)
taxa_importacao = calcular_imposto(valor_compra_real)
valor_final_real = calcular_valor_final(valor_compra_dolar)

print(f'Valor da compra em dólar (sem imposto): {valor_compra_dolar:.2f}')
print(f'Valor da compra em real (sem imposto): {valor_compra_real:.2f}')
print(f'Valor da taxa de importação (em real): {taxa_importacao:.2f}')
print(f'Valor final da compra (em real): {valor_final_real:.2f}')