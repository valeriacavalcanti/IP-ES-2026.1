num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

maior = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

print(maior)