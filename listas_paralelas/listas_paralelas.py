from funciones_listas import *
from data_info import nombres, generos
from random import randint

def mostrar_alumno(legajos:list, nombres:list, generos:list, nota_p1:list, nota_p2:list, proms:list) -> None:
    print(f"{legajos} {nombres} {generos} {nota_p1} {nota_p2} {proms} ")


def mostrar_alumnos(legajos:list, nombres:list, generos:list, nota_p1:list, nota_p2:list, proms:list) -> None:
    size = len(size)
    print("               */*alumnos*/*                ")
    print(" Legajo    nombre    generos    notap1    notap2    promedio")

    for i in range(size):
        mostrar_alumno(legajos[i], nombres[i], generos[i], nota_p1[i], nota_p2[i], proms[i])
    print()


def cargar_alumnos(legajos, nombres, generos, notes_p1, notes_p2, proms, cantidad) -> None:
    cargar_legajos_lista(legajos,cantidad)
    cargar_nombres(nombres,nombres,cantidad)
    cargar_generos(generos, generos, cantidad)
    cargar_notas(notes_p1, cantidad)
    cargar_notas(notes_p2, cantidad)
    promediar_listas(notes_p1, notes_p2, proms)



def cargar_nombres(lista:list, nombres:list, cant:int) -> None:
    cargar_datos_en_lista(lista, nombres, cant)


def cargar_generos(lista:list, generos:list, cant:int) -> None:
    cargar_datos_en_lista(lista, generos, cant)


def cargar_datos_en_lista(lista_destino:list, lista_origen:list, cant:int) -> None:
    if cant <= len(lista_origen):
        for i in range(cant):
            lista_destino.append(lista_origen[i])


def cargar_notas(lista:list, cantidad:int) -> None:
    nota_min = 0
    nota_max = 10
    cargar_lista_random(lista, cantidad, nota_min, nota_max)


def promediar_listas(lista_a:list, lista_b:list, lista_promedios:list) -> None:
    tam = len(lista_a)
    for i in range(tam):
        promedio = calcular_promedioab(lista_a[i], lista_b[i])
        lista_promedios.append(promedio)


def cargar_legajos_lista(lista:list, cantidad:int) -> None:
    legajo_min = 20000
    legajo_max = 30000
    for _ in range(cantidad):
        legajo = randint(legajo_min, legajo_max)
        while entero_in_lista(lista, legajo):
            legajo = randint(legajo_min, legajo_max)
        lista.append(legajo)


size = 10
test = []

cargar_legajos_lista(test, size)
print(test)

cargar_alumnos(legajos, nombres, generos, notes_p1, notes_p2, proms, cantidad)