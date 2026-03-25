def eh_positivo(valor: int) -> bool:
    if valor > 0:
        return True
    else:
        return False

def maior_valor_3(valor1:int, valor2:int, valor3:int) -> int:
    if (valor1 > valor2) and (valor1 > valor3):
        return valor1
    elif (valor2 > valor3):
        return valor2
    else:
        return valor3

def maior_valor_4(valor1:int, valor2:int, valor3:int, valor4:int)->int:
    maior = maior_valor_3(valor1, valor2, valor3)
    if valor4 > maior:
        return valor4
    else:
        return maior

# Testes das Funções
'''
print(eh_positivo(10))
print(eh_positivo(0))
print(eh_positivo(-10))

print(maior_valor_3(10,20,30))
print(maior_valor_3(30,20,10))
print(maior_valor_3(10,10,30))
print(maior_valor_3(10,30,30))
print(maior_valor_3(10,10,10))
print(maior_valor_3(10,20,-30))

print(maior_valor_4(10,20,30,40))
print(maior_valor_4(30,20,10,5))
'''
print(maior_valor_3(10.1,20.2,30.3))

