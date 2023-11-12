import math  

def calcular_area_circulo(radio):
    if radio < 0:
        return "El radio no puede ser negativo"
    else:
        area = math.pi * (radio ** 2)
        return area
radio = float(input("Ingresa el radio del círculo: "))

area = calcular_area_circulo(radio)
if type(area) == str:
    print(area)
else:
    print("El área del círculo con radio", radio, "es:", area)
