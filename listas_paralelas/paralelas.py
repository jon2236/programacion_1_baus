from funciones_listas import *


TAM = 3

legajos = []
nombres = []
generos = []
notas_p1 = []
notas_p2 = []
promedios = []

for _ in range(TAM):
    while True:
        aux = input("Ingrese un legajo entre 20000 y 30000: ")
        if aux.isdigit():
            aux = int(aux)
            if aux >= 20000 and aux <= 30000:
                legajos.append(aux)
                break
            else:
                print("ERROR: El legajo debe estar entre 20000 y 30000 inclusive")
        else:
            print("ERROR: La entrada no es un número entero")


    while True:
        aux = input("ingrese nombre: ")
        if aux.isalpha():
            if len(aux) <= 3 or len(aux) >= 15:
                print("ERROR: caracteres fuera de parametros, re ingrese su nombre con mas de tres letras y menos de 15")
            else:
                nombres.append(aux)
                break
        else:
            print("error, el nombre no puede tener numeros. Re ingrese su nombre con no menos de 3 letras y no mas de 15")


    
    while True:
        aux = input("ingrese genero: m or f ")
        if aux == "m" or aux == "f":
            generos.append(aux)
            break
        else:
            print("error: la entrada debe ser f or m")


    while True:
        aux = (input("ingrese nota parcial 1, entre 0 y 10: "))
        if aux.isdigit():
            aux = int(aux)
            if aux >= 0 and aux <= 10:
                notas_p1.append(aux)
                break
            else:
                print("error: fuera de rango")
        else:
            print("error: se esperaba un numero")


    while True:
        aux = (input("ingrese nota parcial 2, entre 0 y 10: "))
        if aux.isdigit():
            aux = int(aux)
            if aux >= 0 and aux <= 10:
                notas_p2.append(aux)
                break
            else:
                print("error: fuera de rango")
        else:
            print("error: se esperaba un numero")


    promedios.append(calcular_promedioab(notas_p1[-1], notas_p2[-1]))

print(notas_p1)
mostrar_alumnos(legajos, nombres, generos, notas_p1, notas_p2, promedios)
