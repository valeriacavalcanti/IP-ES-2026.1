arq = open('dados.csv', 'r')

registros = arq.read().splitlines()

for i in range(len(registros)):
    print(i, registros[i])


arq.close()
