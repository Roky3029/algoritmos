# Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)

n = int(input('Introduce un número: '))
factorial_base = 1
resultado = 1

while n < 1:
    n = int(input('Rango incorrecto\nIntroduce un número: '))

while not factorial_base == (n + 1):
  resultado = resultado * factorial_base
  factorial_base += 1

print(f'Resultado: {n}! = {resultado}')