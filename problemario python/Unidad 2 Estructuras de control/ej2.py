
numero = int(input("Ingresa un número entero no negativo: "))
factorial = 1
if numero == 0:
    print("El factorial de 0 es 1")
else:
    while numero > 0:
        factorial *= numero
        numero -= 1

    print("El factorial es:", factorial)
