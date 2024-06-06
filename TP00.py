from prog_funcional.funciones_prog import *
from tp_stark.data_stark import lista_personajes
altura_a_float(lista_personajes)
peso_a_float(lista_personajes)



#B
nombres_super_h = mapear_lista(lambda nombres_pj : nombres_pj["nombre"], lista_personajes)
print(nombres_super_h)
print()

#C
nombres_y_altura_super_h = mapear_lista(lambda nombre_pj_y_altura : (nombre_pj_y_altura["nombre"], nombre_pj_y_altura["altura"]), lista_personajes)
print(nombres_y_altura_super_h)
print()

#D
super_h_mas_alto = reduce(lambda heroe_mas_alto, heroe_nuevo_mas_alto : heroe_mas_alto if (heroe_mas_alto["altura"]) > (heroe_nuevo_mas_alto["altura"]) else heroe_nuevo_mas_alto, lista_personajes)

print(f"El superhéroe más alto es {super_h_mas_alto['nombre']} con una altura de {super_h_mas_alto['altura']}")
print()

#E y G
super_h_mas_bajo = reduce(lambda heroe_mas_bajo, heroe_nuevo_mas_bajo : heroe_mas_bajo if (heroe_mas_bajo["altura"]) < (heroe_nuevo_mas_bajo["altura"]) else heroe_nuevo_mas_bajo, lista_personajes)

print(f"El superhéroe más bajo es {super_h_mas_bajo['nombre']} con una altura de {super_h_mas_bajo['altura']}")
print()

#F
promedio_altura = calcular_promedio(mapear_lista(lambda super_h: super_h["altura"], lista_personajes))

print(f"el promedio de altura es {promedio_altura}")

#H
super_h_mas_pesado = reduce(lambda heroe_mas_pesado, heroe_nuevo_mas_pesado : heroe_mas_pesado if (heroe_mas_pesado["peso"]) > (heroe_nuevo_mas_pesado["peso"]) else heroe_nuevo_mas_pesado, lista_personajes)
print(f"El superhéroe más pesado es {super_h_mas_pesado['nombre']} con un peso de {super_h_mas_pesado['peso']}")
print()

super_h_menos_pesado = reduce(lambda heroe_menos_pesado, heroe_nuevo_menos_pesado : heroe_menos_pesado if (heroe_menos_pesado["peso"]) < (heroe_nuevo_menos_pesado["peso"]) else heroe_nuevo_menos_pesado, lista_personajes)
print(f"El superhéroe menos pesado es {super_h_menos_pesado['nombre']} con un peso de {super_h_menos_pesado['peso']}")
print()

#I
def mostrar_nombres_heroes():
    nombres_super_h = mapear_lista(lambda nombres_pj : nombres_pj["nombre"], lista_personajes)
    print(nombres_super_h)
    print()


def mostrar_heroe_y_altura():
    nombres_y_altura_super_h = mapear_lista(lambda nombre_pj_y_altura : (nombre_pj_y_altura["nombre"], nombre_pj_y_altura["altura"]), lista_personajes)
    print(nombres_y_altura_super_h)
    print()


def mostar_heroe_mas_alto():
    super_h_mas_alto = reduce(lambda heroe_mas_alto, heroe_nuevo_mas_alto : heroe_mas_alto if (heroe_mas_alto["altura"]) > (heroe_nuevo_mas_alto["altura"]) else heroe_nuevo_mas_alto, lista_personajes)
    print(f"El superhéroe más alto es {super_h_mas_alto['nombre']} con una altura de {super_h_mas_alto['altura']}")
    print()


def mostar_heroe_mas_bajo():
    super_h_mas_bajo = reduce(lambda heroe_mas_bajo, heroe_nuevo_mas_bajo : heroe_mas_bajo if (heroe_mas_bajo["altura"]) < (heroe_nuevo_mas_bajo["altura"]) else heroe_nuevo_mas_bajo, lista_personajes)
    print(f"El superhéroe más bajo es {super_h_mas_bajo['nombre']} con una altura de {super_h_mas_bajo['altura']}")
    print()


def promedio_altura():
    promedio_altura = calcular_promedio(mapear_lista(lambda super_h: super_h["altura"], lista_personajes))
    print(f"el promedio de altura es {promedio_altura}")


def mostar_heroe_mas_pesado():
    super_h_mas_pesado = reduce(lambda heroe_mas_pesado, heroe_nuevo_mas_pesado : heroe_mas_pesado if (heroe_mas_pesado["peso"]) > (heroe_nuevo_mas_pesado["peso"]) else heroe_nuevo_mas_pesado, lista_personajes)
    print(f"El superhéroe más pesado es {super_h_mas_pesado['nombre']} con un peso de {super_h_mas_pesado['peso']}")
    print()


def mostar_heroe_menos_pesado():
    super_h_menos_pesado = reduce(lambda heroe_menos_pesado, heroe_nuevo_menos_pesado : heroe_menos_pesado if (heroe_menos_pesado["peso"]) < (heroe_nuevo_menos_pesado["peso"]) else heroe_nuevo_menos_pesado, lista_personajes)
    print(f"El superhéroe menos pesado es {super_h_menos_pesado['nombre']} con un peso de {super_h_menos_pesado['peso']}")
    print()

#J
continuar = "s"

while continuar.lower() == "s":
    menu_heroes()
    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        mostrar_nombres_heroes()
    elif opcion == "2":
        mostrar_heroe_y_altura()
    elif opcion == "3":
        mostar_heroe_mas_alto()
    elif opcion == "4":
        mostar_heroe_mas_bajo()
    elif opcion == "5":
        promedio_altura()
    elif opcion == "6":
        mostar_heroe_mas_pesado()
    elif opcion == "7":
        mostar_heroe_menos_pesado()
    elif opcion == "0":
        salir = input("¿Confirma salida? (s/n): ").lower()
        if salir == "s":
            continuar = "n"
    else:
        print("opción no válida. intente nuevamente.")


    pausar()
