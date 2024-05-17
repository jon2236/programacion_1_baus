def factorial(n:int) -> int:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

for numero in range(5):
    print(factorial(numero))


def calcular_factorial(n:int) -> int:
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)

    return resultado

numero = 5
factorial = calcular_factorial(numero)

print(f"el factorial de {numero} es {factorial}")


