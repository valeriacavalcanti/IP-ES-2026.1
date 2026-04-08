# Tempo da natação
hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))
tempo_natacao = (hora * 3600) + (minuto * 60) + segundo

# Tempo do ciclismo
hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))
tempo_ciclismo = (hora * 3600) + (minuto * 60) + segundo

# Tempo da corrida
hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))
tempo_corrida = (hora * 3600) + (minuto * 60) + segundo

# Tempo da prova (soma dos tempos de cada modalidade)
tempo_triatlo = tempo_natacao + tempo_ciclismo + tempo_corrida

# conversão do tempo de prova para hora, minuto e segundo
hora = tempo_triatlo // 3600
minuto = (tempo_triatlo % 3600) // 60
segundo = (tempo_triatlo % 3600) % 60

print(f'{hora}:{minuto}:{segundo}')