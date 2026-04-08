mes = int(input('Código do mês: '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias = 31
elif mes == 2:
    dias = 28
else:
    dias = 30

print(f'{dias} dias')