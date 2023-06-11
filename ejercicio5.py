# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. La fórmula para la conversión es: C = (F-32)*5/9

temperatura = int(input('Dame la temperatura como número entero y en grados Fahrenheit: '))

print(f'{temperatura}ºF = {round((temperatura - 32) * (5/9), 2)}ºC')