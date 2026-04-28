while True:
    num = int(input())

    if num == 0:
        break

    for i in range(1, num):
        print(i, end=' ')
        
    print(num)
