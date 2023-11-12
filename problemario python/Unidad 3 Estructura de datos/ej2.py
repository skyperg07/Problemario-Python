entrada_usuario = input("Ingresa una lista de números separados por comas: ")

numeros_como_cadenas = entrada_usuario.split(',')
numeros = [int(numero) for numero in numeros_como_cadenas]

suma = sum(numeros)

print("La suma de los números es:", suma)
