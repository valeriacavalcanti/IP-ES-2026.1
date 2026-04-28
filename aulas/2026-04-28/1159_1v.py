while True:
    num = int(input())

    if num == 0:
        break

    if num % 2 == 1:
        num += 1

    soma = 0
    for i in range(num, num + 9, 2):
        soma += i

    print(soma)
