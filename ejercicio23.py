# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

cantidad = int(input('¿Cuántos números quieres introducir? '))
lista_n = []

def evaluar_n(n):
    if n < 0:
        return 'menor'
    if n > 0:
        return 'mayor'
    return 'igual'

while not cantidad == 0:
    n = int(input('Introduce un número: '))
    lista_n.append(n)
    cantidad -= 1


print(f'\n\nEvaluación de {lista_n}\n')
for x in lista_n:
    print(f'{x} es evaluado como {evaluar_n(x)} a 0')