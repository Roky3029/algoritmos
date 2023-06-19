# Programa que lea una cadena por teclado y compruebe si es una está escrita en mayúsculas.

texto = input('Escribe un texto: ')

if texto.isupper():
  print('El texto esta escrito en mayusculas')
  exit()
  
print('El texto no esta escrito en mayusculas')