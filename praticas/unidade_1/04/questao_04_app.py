from questao_04_funcoes import *

idade1 = int(input('Idade:'))
altura1 = float(input('Altura: '))
peso1 = float(input('Peso: '))
salario1 = float(input('Salário: '))

idade2 = int(input('Idade:'))
altura2 = float(input('Altura: '))
peso2 = float(input('Peso: '))
salario2 = float(input('Salário: '))

print('Maior idade: ')
print(maior_valor(idade1, idade2))

print('Maior altura: ')
print(maior_valor(altura1, altura2))

print('Maior peso: ')
print(maior_valor(peso1, peso2))

print('Maior salário: ')
print(maior_valor(salario1, salario2))
