# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

n1 = int(input('Dame el primer número: '))
n2 = int(input('Dame un segundo número: '))

print(f'La suma de los números vale: {n1 + n2}')
print(f'Las restas de {n1} y {n2} valen: \n{n1} - {n2} = {n1 - n2}\n{n2} - {n1} = {n2 - n1}')
print(f'El producto de ambos números es: {n1 * n2}')
print(f'Los cocientes de {n1} y {n2} valen: \n{n1} / {n2} = {n1 / n2}\n{n2} / {n1} = {n2 / n1}')
