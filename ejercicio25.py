# Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

prod1 = int(input('Introduce un número: '))
prod2 = 1

while prod2 <= 10:
    print(f'{prod1} * {prod2} = {prod1 * prod2}')
    prod2 += 1