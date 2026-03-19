# ler a nota de um estudante e aumentar em 20%

nota = int(input('Nota: '))

'''
if nota >= 0:
    if nota <= 100:
        print('nota entre 0 e 100')
    else:
        print('nota acima de 100')
else:
    print('nota abaixo de 0')
'''

if (nota >= 0) and (nota <= 100):
    aumento = nota * 0.2
    nota = nota + aumento
    if (nota > 100):
        nota = 100
    print(f'{nota=}')
else:
    print('Nota inválida')
    
