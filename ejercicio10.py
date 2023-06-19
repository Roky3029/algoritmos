# Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

n1 = int(input('Dame un número: '))
n2 = int(input('Dame otro número: '))

if n1 > n2:
  print(f'{n1} es mayor que {n2}')
  exit()

print(f'{n1} NO es mayor que {n2}')