def sumar() -> None:
    """pide 2 numeros por consola, los suma y muestra en consola el resultado
    """
    num1 = int(input("ingrese un numero: "))
    num2 = int(input("ingrese otro numero"))

    resultado = num1 + num2

    print(f"la suma es {resultado}")

sumar()


def multiplo(a:int, b:int) -> bool:

    
    """verifica si un numero es multiplo de otro

    args:
        valor (int): numero a verificar
    
    returns:
        int: retorna el multiplo
    """
    retorno = False
    if a % b == 0:
        retorno = True

    return retorno

num_1 = int(input("ingrese un numero"))
num_2 = int(input("ingrese un numero"))

print(multiplo(num_1, num_2))



def calcular_perimetro_circunferencia(radio: int) -> float:
    from math import pi
    return 2 * radio * pi

num_1 = int(input("ingrese un numero para calcular pi"))

print(calcular_perimetro_circunferencia(num_1))





def calcular_perimetro_rectangulo(base:int, altura:int) -> int:
    return 2 * (base + altura)

num1 = int(input("ingrese un base"))
num2 = int(input("ingrese altura"))

print(calcular_perimetro_rectangulo(num1, num2))





def calcular_perimetro_cuadrado(lado:int) -> int:
    return 4 * (lado)

num1 = int(input("ingrese lado"))

print(calcular_perimetro_cuadrado(num1))





