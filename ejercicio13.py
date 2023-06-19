# Escribe un programa que lea un número e indique si es par o impar.

n = int(input('Dame un número: '))

if n % 2:
  print(f'{n} es impar')
  exit()

print(f'{n} es par')