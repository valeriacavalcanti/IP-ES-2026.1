# ler o nome e a idade de 6 pessoas, ao final, exiba o(s) nome(s) da(s)
# pessoa (s) mais nova.

nomes = [''] * 6
idades = [0] * 6

for i in range(6):
    nomes[i] = input('Nome: ')
    idades[i] = int(input('Idade: '))

# descobrir o menor valor
menor = idades[0]

for i in range(6):
    if idades[i] < menor:
        menor = idades[i]

# descobrir quem tem essa menor idade
for i in range(6):
    if idades[i] == menor:
        print(nomes[i])

        
