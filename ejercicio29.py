# Realizar un algoritmo que permita descomponer un número en sus factores primos.

n = int(input("Ingrese numero: "))

primos = []
for i in range(2, n + 1):
    while n % i == 0:
        primos.append(i)
        n = n / i
        
print(f'Factores primos: {primos}')