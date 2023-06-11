from math import sqrt

# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto1 = int(input('Dame la longitud de uno de los catetos del triángulo rectángulo (m): '))
cateto2 = int(input('Dame la longitud del otro cateto del triángulo rectángulo (m): '))

print(f'La hipotenusa de ese triangulo vale: {round(sqrt((cateto1 ** 2) + (cateto2 ** 2)), 3)}m')