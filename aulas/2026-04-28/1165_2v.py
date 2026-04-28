def e_primo(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


##

qtd = int(input())

for i in range(qtd):
    num = int(input())

    if e_primo(num):
        print(num, 'eh primo')
    else:
        print(num,'nao eh primo')
