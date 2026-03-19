# dias da semana

'''
dom 0
seg 1
ter 2
qua 3
qui 4
sex 5
sab 6
'''

codigo_dia = input('Código do dia da semana: ')

if codigo_dia == '0':
    print('dom')
if codigo_dia == '1':
    print('seg')
if codigo_dia == '2':
    print('ter')
if codigo_dia == '3':
    print('qua')
if codigo_dia == '4':
    print('qui')
if codigo_dia == '5':
    print('sex')
if codigo_dia == '6':
    print('sab')
if codigo_dia < '0' or codigo_dia > '6':
    print('opcao inválida')

