import random

menor, maior = 1, 100
sorteio = random.randint(menor, maior)
print(sorteio)

while True:
    chute = int(input(f'Chute ({menor} e {maior}): '))

    if chute == sorteio:
        break

    print('Eita! Errou!')
    if chute > sorteio:
        print('Seu chute é maior')
        maior = chute - 1
    else:
        print('Seu chute é menor')
        menor = chute + 1

print(chute, sorteio)
