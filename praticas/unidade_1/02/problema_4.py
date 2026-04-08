valor_compra = float(input('Valor da compra: '))
qtd_cupons = int(valor_compra/20)

valor_novo_cupom = 20 - (valor_compra % 20)
# valor_novo_cupom = 20 - (valor_compra - (qtd_cupons * 20))

print(f'Quantidade de cupons: {qtd_cupons}')
print(f'Valor para novo cupom: {valor_novo_cupom}')