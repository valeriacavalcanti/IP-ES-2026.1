qtd = int(input())

for i in range(qtd):
    num = int(input())

    # verificar se e primo
    e_primo = True
    for i in range(2, num):
        if num % i == 0:
            e_primo = False
            break

    if e_primo == True:
        print(num, 'eh primo')
    else:
        print(num,'nao eh primo')
