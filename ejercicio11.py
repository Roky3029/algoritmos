# Modifica el ejercicio anterior para que diga cuál de los dos números es mayor o si son iguales.

n1 = int(input('Dame un número: '))
n2 = int(input('Dame otro número: '))

if n1 > n2:
  print(f'{n1} es mayor que {n2}')
  exit()

if n2 > n1:
  print(f'{n2} es mayor que {n1}')
  exit()

print(f'{n1} es igual que {n2}')