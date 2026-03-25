def maior_valor_3(valor1:int, valor2:int, valor3:int) -> int:
    if (valor1 > valor2) and (valor1 > valor3):
        return valor1
    elif (valor2 > valor3):
        return valor2
    else:
        return valor3

def forma_triangulo(l1:int, l2:int, l3:int) -> bool:
    maior_lado = maior_valor_3(l1, l2, l3)
    soma = l1 + l2 +l3 - maior_lado

    return maior_lado < soma
    '''
    if maior_lado < soma:
        return True
    else:
        return False
    '''

def tipo_triangulo(l1:int, l2:int, l3:int) -> str:

    if (l1 == l2 and l1 == l3):
        return 'equilatero'
    elif (l1 != l2 and l1 != l3 and l2 != l3):
        return 'escaleno'
    else:
        return 'isosceles'


# testes
'''
print(forma_triangulo(3, 4, 5))
print(forma_triangulo(3, 3, 3))
print(forma_triangulo(3, 2, 3))
print(forma_triangulo(1, 2, 3))

print(tipo_triangulo(3, 4, 5))
print(tipo_triangulo(3, 3, 3))
print(tipo_triangulo(3, 2, 3))
'''
