from questao_05_funcoes import comparar
from datetime import datetime

def converter_em_dias(dia: int, mes: int, ano: int) -> int:
    return dia + (mes * 30) + (ano * 365)


## PP

# Obter a data atual do sistema
agora = datetime.now()
dias_agora = converter_em_dias(agora.day, agora.month, agora.year)

# Obter a data de validade do usuário
dia_validade = int(input('Dia da validade: '))
mes_validade = int(input('Mês da validade: '))
ano_validade = int(input('Ano da validade: '))

dias_validade = converter_em_dias(dia_validade, mes_validade, ano_validade)


# Comparar as duas datas convertidas em "dias"

resposta = comparar(dias_validade, dias_agora)
if resposta == -1:
    print('O produdo está vencido')
elif resposta == 0:
    print('O produto deve ser consumido hoje')
else:
    print('O produto está apto para consumo')
