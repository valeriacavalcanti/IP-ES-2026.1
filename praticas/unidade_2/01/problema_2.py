num1, num2 = input('Números: ').split()
num1, num2 = int(num1), int(num2)

qtd_igual = 0

while num1 > 0 and num2 > 0:
    if num1 == num2:
        qtd_igual = qtd_igual + 1

    num1, num2 = input('Números: ').split()
    num1, num2 = int(num1), int(num2)

print(qtd_igual)