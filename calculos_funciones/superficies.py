from math import pi

def calcular_superficie_circulo(radio:int) -> int:
    return pi * (radio ** 2)



def calcular_superficie_rectangulo(longitud:int, ancho:int) -> int:
    return longitud * ancho



def calcular_superficie_cuadrado(lado:int) -> int:
    return lado * lado



def calcular_superficie_triangulo(base:int, altura:int) -> int:
    return base * altura / 2


print(calcular_superficie_circulo(4))