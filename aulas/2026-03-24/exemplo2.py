def maior_valor_3(valor1:int, valor2:int, valor3:int) -> int:
    if (valor1 > valor2) and (valor1 > valor3):
        maior = valor1
    elif (valor2 > valor3):
        maior = valor2
    else:
        maior = valor3
    return maior
    print('que bom')

## PP
print(maior_valor_3(1,2,3))
