l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

# descobrir o maior lado
if l1 > l2 and l1 > l3:
    maior = l1
elif l2 > l3:
    maior = l2
else:
    maior = l3

# soma dos demais lados
soma_lados = l1 + l2 + l3 - maior

# verificar se forma triângulo
if maior < soma_lados:
    if l1 == l2 and l1 == l3:
        print('Triângulo Equilátero')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Não forma triângulo')