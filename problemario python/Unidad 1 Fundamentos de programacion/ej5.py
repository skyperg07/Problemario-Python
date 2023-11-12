
N = int(input("Ingresa un número entero positivo N: "))
suma = 0
for numero in range(1, N + 1):
    suma += numero

print("La suma de los primeros", N, "números naturales es:", suma)
