# Escribir por pantalla cada carácter de una cadena introducida por teclado.

from time import sleep

texto = input('Introduce un texto: ')
caracteres = []

for caracter in texto:
    caracteres.append(caracter)

for char in caracteres:
    sleep(0.25)
    print(char)