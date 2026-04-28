def converte(hora: int, minuto: int, segundo: int) -> int:
    return hora * 3600 + minuto * 60 + segundo

def hora(segundos: int) -> int:
    return segundos // 3600

def minuto(segundos: int) -> int:
    return segundos % 3600 // 60

def segundo(segundos: int) -> int:
    return segundos % 3600 % 60
