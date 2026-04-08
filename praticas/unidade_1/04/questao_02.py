def celcius_para_fahrenheit(temperatura: float) -> float:
    return (temperatura * 9/5) + 32

def celcius_para_kelvin(temperatura: float) -> float:
    return temperatura + 273.15

## PP

temperatura_celcius = float(input('Informe a temperatura em Celcius: '))
temperatura_fahrenheit = celcius_para_fahrenheit(temperatura_celcius)
temperatura_kelvin = celcius_para_kelvin(temperatura_celcius)

print(f'Temperatura em Celcius: {temperatura_celcius}')
print(f'Temperatura em Fahrenheit: {temperatura_fahrenheit}')
print(f'Temperatura em Kelvin: {temperatura_kelvin}')