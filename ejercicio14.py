# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

from time import sleep

n1 = int(input('Dame un número: '))
n2 = int(input('Dame otro número: '))

if n2 == 0:
  print('¡ALERTA!')
  sleep(0.5)
  print('¡ALERTA!')
  sleep(0.5)
  print('¡ALERTA!')
  sleep(0.5)
  print('No se puede dividir por 0')
  exit()

print(f'{n1} / {n2} = {n1 / n2}')