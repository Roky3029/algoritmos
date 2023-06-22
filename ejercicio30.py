# Haz un programa que te pregunte por un nº de DNI, y calcule la letra. La letra se calcula dividiendo el DNI entre 23, el resto será un valor del 0 al 22, que será la posición de la cadena "TRWAGMYFPDXBNJZSQVHLCKE"

n = int(input('Dame tu número del DNI: '))
posibles_letras = 'TRWAGMYFPDXBNJZSQVHLCKE'

while len(str(n)) != 8:
  n = int(input('Error. El DNI tiene solo 8 números. Ejemplo: 12345678\nDame tu número del DNI: '))

posicion_letra = n % 23
letra = posibles_letras[posicion_letra]

print(f'La letra sería la {letra}\nEl DNI completo sería: {n}{letra}')