# Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si acaba en 00 (es decir, es divisible por 100) salvo que también sea divisible por 400.

# Ejemplos: 
# 1800 no es bisiesto, porque aunque es divisible por 4, también lo es por 100 y no por 400.
# 2000 es bisiesto, porque es divisible por 4 y aunque también lo es por 100, lo es por 400.

year = int(input('Introduce un año: '))

def divisible_by_n(year, divisor):
    return not year % divisor # Si year es divisible entre divisor, devolvera true

divisible_by_4 = divisible_by_n(year, 4)
divisible_by_100 = divisible_by_n(year, 100)
divisible_by_400 = divisible_by_n(year, 400)

if ((divisible_by_4 and not divisible_by_100) or divisible_by_400):
    print(f'El año {year} es bisiesto')
    exit()


print(f'El año {year} NO es bisiesto')