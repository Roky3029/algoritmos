# Ejercicio 19 
# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje:
#  “ERROR: número incorrecto.”.
# Ejemplo:
# Introduzca número del dado: 5
# En la cara opuesta está el "dos".

n = int(input('Introduce un número: '))

while n < 1 or n > 6:
    n = int(input('Rango incorrecto\nIntroduce un número: '))

caras_opuestas = {
    1: 6,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1
}

print(f'El número {n} tiene como cara opuesta el {caras_opuestas[n]}')