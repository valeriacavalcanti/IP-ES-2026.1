# calcular o valor da compra a partir do valor unitário e a quantidade comprada
def calcular_valor_compra(valor_dolar: float, qtd_comprada: int) -> float:
    return valor_dolar * qtd_comprada


# converter um valor de dólar para real. Considerando que 1 dólar vale 5 reais
def converter_dolar_para_real(valor_dolar: float) -> float:
    return valor_dolar * 5


# calcular o imposto de importação a partir do valor da compra em real.
def calcular_imposto(valor_real: float) -> float:
    if valor_real <= converter_dolar_para_real(50):
        imposto = valor_real * 0.2
    else:
        imposto = valor_real * 0.6
    return imposto


# calcular o valor final da compra, que é o somatório do valor da compra + imposto
def calcular_valor_final(valor_dolar: float) -> float:
    valor_real = converter_dolar_para_real(valor_dolar)
    return valor_real + calcular_imposto(valor_real)