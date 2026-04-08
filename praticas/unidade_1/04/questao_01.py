def somar(num1: int, num2: int) -> int:
    return num1 + num2

def maior(num1: int, num2: int) -> int:
    if num1 >= num2:
        return num1
    else:
        return num2

def exibir(num1: int, num2: int):
    print(f'Primeiro número: {num1}')
    print(f'Segundo número: {num2}')

def mensagem_pt():
    return 'Olá, bem-vindo ao programa de operações matemáticas!'

def mensagem_en():
    return 'Hello, welcome to the math operations program!'

def misterio6(idioma: str):
    if idioma == 'pt':
        msg = mensagem_pt()
    else:
        msg = mensagem_en()

    print(msg)

## programa principal

misterio6('pt')

numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))

exibir(numero1, numero2)

soma_valores = somar(numero1, numero2)
maior_valor = maior(numero1, numero2)

print(soma_valores, maior_valor)
