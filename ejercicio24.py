# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

char = None

while not char == ' ':
    char = input('Dame un caracter (Espacio para salir): ').lower()

    if char == ' ':
        continue

    if char in ('a', 'e', 'i', 'o', 'u'):
        print('VOCAL')
        continue
    print('NO VOCAL')