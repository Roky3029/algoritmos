# Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad.

from math import sqrt, floor

n = int(input('Introduce un número: '))
counter = 1
divisores = []

while counter <= n:
    if not n % counter:
        divisores.append(counter)
    counter += 1

if len(divisores) == 2:
    print(f'{n} es primo')
    exit()

print(f'{n} no es primo')