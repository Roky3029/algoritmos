# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

n = int(input('Dame un número entero de 2 cifras: '))

while n > 99 or n < 10:
  n = int(input('Error. El número debe ser de dos cifras\nDame un número entero de 2 cifras: '))
    
unidades = n % 10
decenas = (n - unidades) // 10
print(f'El invertido de {n} es {unidades}{decenas}')