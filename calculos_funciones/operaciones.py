from os import system

def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")

def menu() -> str:
    """_despliega un menu con opciones para interactuar con el usuario

    Returns:
        str: _submenu
    """
    limpiar_pantalla()
    print("      menu de opciones")
    print("A- ingrese su primer operando ")
    print("B- ingrese su segundo operando ")
    print("C- elegir operacion aritmetica ")
    print("D- mostrar mi resultados")
    print("E- salir")
    
    return input("ingrese su operando ")

def ingrese_operando(mensaje:str) -> int:
    """pide un entero a ingresar por un usuario

    Returns:
        int: _entero guardado por usuario
    """
    operando = int(input(mensaje))
    return operando

# def ingrese_segundo_operando(mensaje:str) -> int:
#     """pide un entero a ingresar por un usuario

#     Returns:
#         int: _entero guardado por usuario
#     """
#     operando_2 = int(input(mensaje))
#     return operando_2

def sub_menu() -> str:
    """_despliega un menu con opciones para interactuar con el usuario

    Returns:
        str: _realiza la operacion aritmetica seleccionada
    """
    limpiar_pantalla()
    print("      seleccionar operancion")
    print("1- sumar")
    print("2- restar")
    print("3- multiplicar")
    print("4- dividir")
    print("5- factorial")
    print("6- menu principal")

    return input("ingrese opcion ")

def sumar(num1:int, num2:int) -> int:
    """suma dos enteros

    Args:
        num1 (int): _ingreso primer entero
        num2 (int): _ingreso segundo entero

    Returns:
        int: _resultado de la suma de 2 enteros
    """
    resultado = num1 + num2
    return resultado

def restar(num1:int, num2:int) -> int:
    """resta dos enteros

    Args:
        num1 (int): _ingreso primer entero
        num2 (int): _ingreso segundo entero

    Returns:
        int: _resultado de la resta de 2 enteros
    """
    resultado = num1 - num2
    return resultado

def multiplicar(num1:int, num2:int) -> int:
    """multiplica dos enteros

    Args:
        num1 (int): _ingreso primer entero
        num2 (int): _ingreso segundo entero

    Returns:
        int: _resultado multiplicacion de 2 enteros
    """
    resultado = num1 * num2
    return resultado

def dividir(num1:int, num2:int) -> int:
    """divide dos enteros

    Args:
        num1 (int): _ingreso primer entero
        num2 (int): _ingreso segundo entero

    Returns:
        int: _resultado de la division de 2 enteros
    """
    resultado = num1 / num2
    return resultado

def factorial(num1:int) -> int:
    """calcula un factorial

    Args:
        num1 (int): _ingreso primer entero
        num2 (int): _ingreso segundo entero

    Returns:
        int: _resultado factorial
    """
    facto = 1
    for i in range(2, num1 + 1):
        facto *= i
    return facto