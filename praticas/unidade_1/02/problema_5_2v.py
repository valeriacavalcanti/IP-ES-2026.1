valor_compra = float(input('Valor da compra: '))

pagamento_vista = valor_compra * 0.9
pagamento_credito = valor_compra
pagamento_parcelado = valor_compra * 1.2
valor_parcela = pagamento_parcelado / 4

print(f'Pagamento à vista: {pagamento_vista:.2f}')
print(f'Pagamento com cartão de crédito: {pagamento_credito:.2f}')
print(f'Pagamento parcelado: {pagamento_parcelado:.2f} (4 parcelas de {valor_parcela:.2f})')