lista_original = [1, 2, 2, 3, 4, 5, 8, 9, 9, 4, 5, 6, 6, 7]
lista_sin_duplicados = []
for elemento in lista_original:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)

print("Lista original:", lista_original)
print("Lista sin duplicados:", lista_sin_duplicados)
