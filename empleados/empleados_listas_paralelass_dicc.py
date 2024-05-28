from alumnos_lista.funciones_listas_alumnos import *
from def_listas.data_info import nombres, generos
from random import randint


def mostrar_alumno(un_alumno) -> None:
    print(f"{un_alumno[0]}      {un_alumno[1]:10}      {un_alumno[2]}      {un_alumno[3]:2}      {un_alumno[4]:2}      {un_alumno[5]:5.2f}") #:5 caracteres .2f con 2 decimalesa


def mostrar_alumnos(alumnos:list) -> None:
    tam = len(alumnos)
    print("                 Lista de Alumnos")
    print("Legajo     Nombre       Genero   NotaP1   NotaP2   Promedio")
    print("------------------------------------------------------------------------")
    for i in range(tam):
        mostrar_alumno(alumnos[i])
    print()


def cargar_alumnos(lista:list, cantidad):
    legs = []
    names = []
    gender = []
    notes_p1 = []
    notes_p2 = []
    cargar_legajos_lista(legs, cantidad)
    cargar_datos_en_lista(gender, generos, cantidad)
    cargar_datos_en_lista(names, nombres, cantidad)
    cargar_notas(notes_p1, cantidad)
    cargar_notas(notes_p2, cantidad)
    for i in range(cantidad):
        lista.append(nuevo_alumno(legs[i], names[i], gender[i], notes_p1[i], notes_p2[i]))



def nuevo_alumno(legajo:int, nombre:str, genero:str, nota_p1:int, nota_p2:int) -> list:
    nuevo_alumno = []
    nuevo_alumno.append(legajo)
    nuevo_alumno.append(nombre)
    nuevo_alumno.append(genero)
    nuevo_alumno.append(nota_p1)
    nuevo_alumno.append(nota_p2)
    nuevo_alumno.append(calcular_promedioab(nota_p1, nota_p2))
    return nuevo_alumno


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


def promediar_notas_alumnos(valor_a:int, valor_b:int, lista_promedios:list) -> None:
    promedio = calcular_promedioab(valor_a, valor_b)
    lista_promedios.append(promedio)


def cargar_legajos_lista(lista:list, cantidad:int) -> None:
    legajo_min = 20000
    legajo_max = 30000
    for _ in range(cantidad):
        legajo = randint(legajo_min, legajo_max)
        while entero_in_lista(lista, legajo):
            legajo = randint(legajo_min, legajo_max)
        lista.append(legajo)

