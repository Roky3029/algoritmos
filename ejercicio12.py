# Algoritmo que pida un número y diga si es positivo, negativo o 0.

n = int(input('Dame un número: '))

if n > 0:
  print(f'{n} es positivo')
  exit()

if n < 0:
  print(f'{n} es negativo')
  exit()

print(f'{n} es 0')