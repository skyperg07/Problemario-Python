def calcular_factorial(n):
    if n == 0:
        return 1  # El factorial de 0 es 1
    else:
        return n * calcular_factorial(n - 1)

numero = 25
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es {resultado}")
