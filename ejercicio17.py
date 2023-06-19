# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
# Previamente debe comprobar si los tres números forman un triángulo.
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si los 3 lados son iguales entonces es equilátero.
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

l1 = int(input('Dame la medida del lado A (el mas largo) del triángulo (m): '))
l2 = int(input('Dame la medida del lado B (el segundo mas largo) del triángulo (m): '))
l3 = int(input('Dame la medida del lado C (el mas corto) del triángulo (m): '))

def check_is_triangle(side1, side2, side3):
    if side1 > (side2 + side3):
        print(f'El triángulo de medidas {side1}, {side2} y {side3} es imposible')
        exit()
    if side2 > (side1 + side3):
        print(f'El triángulo de medidas {side1}, {side2} y {side3} es imposible')
        exit()
    if side3 > (side2 + side1):
        print(f'El triángulo de medidas {side1}, {side2} y {side3} es imposible')
        exit()
    
def check_type_of_triangle(side1, side2, side3):
    if ((side1 ** 2) == ((side2 ** 2) + (side3 ** 2))):
        print(f'El triángulo de medidas {side1}, {side2} y {side3} es rectángulo')
        exit()
    if side1 == side2 == side3:
        print(f'El triángulo de medidas {side1}, {side2} y {side3} es equilatero')
        exit()
    if side1 == side2 or side2 == side3 or side1 == side3:
        print(f'El triángulo de medidas {side1}, {side2} y {side3} es isosceles')
        exit()

    print(f'El triángulo de medidas {side1}, {side2} y {side3} es escaleno')

check_is_triangle(l1, l2, l3)
check_type_of_triangle(l1, l2, l3)