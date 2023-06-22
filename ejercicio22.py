# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

lista_n = []
n = None
suma = 0


while not n == 0:
    try:
        n = int(input('Introduce un número (Escribe 0 para parar): '))
    except ValueError:
        n = int(input('Valor introducido incorrecto\nIntroduce un número (Escribe 0 para parar): '))

    if n == 0:
        continue
    
    lista_n.append(n)

for x in lista_n:
    suma += x

media = (suma / len(lista_n))

print(f'La suma de {lista_n} es: {suma}')
print(f'La media de {lista_n} es: {media}')