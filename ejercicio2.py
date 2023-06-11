# Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = int(input('Dame la longitud de la base del rectángulo (m): '))
altura = int(input('Dame la longitud de la altura del rectángulo (m): '))

print(f'Perímetro: {(2 * base) + (2 * altura)}m')
print(f'Área: {base * altura}m²')