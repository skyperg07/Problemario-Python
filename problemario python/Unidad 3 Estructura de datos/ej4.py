entrada_usuario = input("Ingresa una lista de números separados por comas: ")

numeros_como_cadenas = entrada_usuario.split(',')

numeros = [int(numero) for numero in numeros_como_cadenas]

numero_mayor = max(numeros)

print("El número mayor en la lista es:", numero_mayor)
