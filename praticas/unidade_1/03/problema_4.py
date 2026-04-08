temperatura = int(input('Temperatura: '))

if temperatura < 10:
    print('Muito Frio')
elif temperatura <= 15:
    print('Frio')
elif temperatura <= 25:
    print('Agradável')
elif temperatura <= 30:
    print('Quente')
else:
    print('Muito Quente')