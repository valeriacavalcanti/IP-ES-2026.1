from problema4 import *

menor = converte(2,0,1)

for i in range(3):
    nome = input('Nome: ')
    h, m, s = input('Tempo: ').split(':')
    h, m, s = int(h), int(m), int(s)

    tempo = converte(h, m, s)
    if tempo < menor:
        menor = tempo
        nome_menor = nome

h = hora(menor)
m = minuto(menor)
s = segundo(menor)
print(f'Nome: {nome_menor} - {h}:{m}:{s}')
