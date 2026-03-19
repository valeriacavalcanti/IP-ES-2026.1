# Programa para ler 3 notas. 
# Calcular e exibir:
#  - As notas lidas;
#  - A média da pessoa.


'''
Programa para ler 3 notas.
Calcular e exibir:
- As notas lidas;
- A média da pessoa.
'''

#nota_1 = int(input('Nota 1: '))
#nota_2 = int(input('Nota 2: '))
#nota_3 = int(input('Nota 3: '))

nota_1, nota_2, nota_3 = input('Digite suas 3 notas: ').split()
nota_1 = int(nota_1)
nota_2 = int(nota_2)
nota_3 = int(nota_3)

media = (nota_1 + nota_2 + nota_3)/3

#print('Nota 1 =', nota_1, 'Nota2 =', nota_2, 'Nota3 =', nota_3)
print(f'Nota 1: {nota_1}\nNota 2: {nota_2}\nNota 3: {nota_3}')
print(f'Média: {media:.0f}')
