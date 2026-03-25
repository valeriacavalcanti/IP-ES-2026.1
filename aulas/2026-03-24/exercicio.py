#from triangulo import maior_valor_3
import triangulo

lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if triangulo.forma_triangulo(lado1, lado2, lado3):
    print(triangulo.tipo_triangulo(lado1, lado2, lado3))
else:
    print('Não forma triangulo')
