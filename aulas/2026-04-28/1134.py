q_a = q_g = q_d = 0

while True:
    opcao = input()

    if opcao == '1':
        q_a += 1
    elif opcao == '2':
        q_g += 1
    elif opcao == '3':
        q_d += 1
    elif opcao == '4':
        break

print('MUITO OBRIGADO')
print(f'Alcool: {q_a}')
print(f'Gasolina: {q_g}')
print(f'Diesel: {q_d}')
