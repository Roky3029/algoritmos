# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

dias_semana = {
    1: 'lunes',
    2: 'martes',
    3: 'miercoles',
    4: 'jueves',
    5: 'viernes',
    6: 'sabado',
    7: 'domingo'
}

n = int(input('Introduce un número correspondiente a un dia de la semana: '))

while n < 1 or n > 7:
    n = int(input('Rango incorrecto\nIntroduce un número: '))

print(f'El dia nº{n} de la semana es {dias_semana[n]}')