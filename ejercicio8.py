# Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

from math import sqrt

n = int(input('Dame un número entero: '))

print(f'La raiz cuadrada de {n} es {round(sqrt(n), 2)}')
print(f'La raiz cubica de {n} es {round(n ** (1/3), 2)}')