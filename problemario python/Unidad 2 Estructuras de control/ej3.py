
N = int(input("Ingresa un número entero positivo para N: "))
a, b = 0, 1
if N <= 0:
    print("Por favor, ingresa un número entero positivo para N.")
elif N == 1:
    print("Los primeros", N, "término(s) de la serie Fibonacci:")
    print(a)
else:
    print("Los primeros", N, "términos de la serie Fibonacci:")
    print(a)
    print(b)
    for _ in range(2, N):
        a, b = b, a + b
        print(b)
