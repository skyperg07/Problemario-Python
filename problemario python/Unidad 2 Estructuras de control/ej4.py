
N = int(input("Ingresa la cantidad de números a promediar: "))
suma = 0
for i in range(N):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    suma += numero

promedio = suma / N

print(f"El promedio de los {N} números ingresados es: {promedio}")
