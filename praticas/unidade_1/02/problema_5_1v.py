valor_compra = float(input('Valor da compra: '))

# pagamento à vista
desconto = valor_compra * 0.1
pagamento_vista = valor_compra - desconto

# pagamento no cartão de crédito (sem alteração)
pagamento_credito = valor_compra

# pagamento parcelado
aumento = valor_compra * 0.2
pagamento_parcelado = valor_compra + aumento
valor_parcela = pagamento_parcelado / 4

print(f'Pagamento à vista: {pagamento_vista:.2f}')
print(f'Pagamento com cartão de crédito: {pagamento_credito:.2f}')
print(f'Pagamento parcelado: {pagamento_parcelado:.2f} (4 parcelas de {valor_parcela:.2f})')