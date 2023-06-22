# Realizar un programa que dada una cadena de caracteres introducidos individualmente, genere otra cadena resultado de invertir la primera.

caracter = None
lista_caracteres = []

while not caracter == '.':
    caracter = input('Introduce un caracter (. para salir): ')
  
    if len(caracter) > 1 or caracter == '':
        caracter = input('Error de rango o espacio en blanco introducido\nIntroduce un caracter (. para salir): ')

    if caracter == '.':
        continue

    lista_caracteres.append(caracter)

print(f'\nDatos originales: {lista_caracteres}\nDatos invertidos: {lista_caracteres[::-1]}')