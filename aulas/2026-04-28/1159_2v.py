while True:
    num = int(input())

    if num == 0:
        break

    if num % 2 == 1:
        num += 1

    soma = 0
    for i in range(5):
        soma += num
        num += 2

    print(soma)
