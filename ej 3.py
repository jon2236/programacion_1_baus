def sumar() -> int:
    """pide 2 numeros por consola, los suma y retorna el resultado

    Args:
        a (int): no recibe nada
        b (int): no recibe nada

    Returns:
        int: retorna el resultado de sumar 2 enteros
    """
    num1 = int(input("ingrese un numero: "))
    num2 = int(input("ingrese otro numero"))

    return num1 + num2


resultado = sumar ()

print(f"la suma es {resultado}")