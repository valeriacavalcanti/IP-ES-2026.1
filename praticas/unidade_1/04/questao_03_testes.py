from questao_03_funcoes import *

# Teste com imposto de 20%

valor_unitario = 10
qtd = 1

valor_compra_dolar = calcular_valor_compra(valor_unitario, qtd)
valor_compra_real = converter_dolar_para_real(valor_compra_dolar)
taxa_importacao = calcular_imposto(valor_compra_real)
valor_final_real = calcular_valor_final(valor_compra_dolar)

assert valor_compra_dolar == 10
assert valor_compra_real == 50
assert taxa_importacao == 10
assert valor_final_real == 60

print('Testes 20% - ok')


# Teste com imposto de 60%

valor_unitario = 100
qtd = 1

valor_compra_dolar = calcular_valor_compra(valor_unitario, qtd)
valor_compra_real = converter_dolar_para_real(valor_compra_dolar)
taxa_importacao = calcular_imposto(valor_compra_real)
valor_final_real = calcular_valor_final(valor_compra_dolar)

assert valor_compra_dolar == 100
assert valor_compra_real == 500
assert taxa_importacao == 300
assert valor_final_real == 800

print('Testes 60% - ok')


''''
Assert é um comando que serve para garantir que uma condição seja verdadeira para programa continuar.

Se a condição for verdadeira, o Python não faz nada e segue para a próxima linha.
Se a condição for falsa, o Python interrompe o programa imediatamente e gera um erro chamado AssertionError.

Podemos usar para testar a nossa função! Se o resultado for igual ao esperado ... segue para o próximo teste!

Se nenhum teste falhar ... a mensagem de sucesso será exibida! Caso contrário, o programa será interrompido onde houve a falha.
'''
