# Calcular la media de tres números pedidos por teclado.

n1 = int(input('Dame el primer número: '))
n2 = int(input('Dame el segundo número: '))
n3 = int(input('Dame el tercer número: '))

print(f'La media de los tres números es: {round((n1 + n2 + n3) / 3, 3)}')