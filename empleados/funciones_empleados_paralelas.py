from funciones_empleados_dicc import *
from data_empleados import *
from random import randint, choice


def mostrar_empleado(empleado: dict):
        print(f"{empleado["legajo"]}{empleado["nombre"]:>10}{empleado["apellido"]:>15}{empleado["genero"]:>5}{empleado["edad"]:>10}{empleado["provincia"]:>15}{empleado["localidad"]:>10}  {empleado["calle"]:>23}{empleado["sector"]:>15}   {empleado["correo"]:>20}")


def mostrar_empleados(lista: list)->None:
    print("\t\t\tListas de Alumnos\t\t\t\n")
    print("Legajo   Nombre      Apellido    Genero   Edad    Provincia     Localidad    Calle                    Sector    Correo")
    for i in range(len(lista)):
        mostrar_empleado(lista[i])
    print()


def new_empleado(legajo:int, nombre:str, apellido: str, genero:str, edad:int, correo:str, calle:str,localidad:str, provincia: str, sector: str, lista:list):
    nuevo_empleado ={}
    nuevo_empleado['legajo'] = validar_legajo(20000, 30000, legajo, lista)
    nuevo_empleado['nombre'] = nombre
    nuevo_empleado['apellido'] = apellido
    nuevo_empleado['genero'] = genero
    nuevo_empleado['edad'] = edad
    nuevo_empleado['correo'] = correo
    nuevo_empleado['calle'] = calle
    nuevo_empleado['localidad'] = localidad
    nuevo_empleado['provincia'] = provincia
    nuevo_empleado['sector'] = sector
    return nuevo_empleado
    


def cargar_empleados(lista:list, cant:int):
    EDAD_MIN = 18
    EDAD_MAX = 68
    LEGAJO_INICIAL = 20000
    next_legajo = LEGAJO_INICIAL
    for _ in range(cant):
        legajo = next_legajo
        next_legajo += 1
        genero = choice(["f", "m"])
        nombre = choice(nombres_m) if genero == "m" else choice(nombres_f)
        apellido = choice(apellidos_data)
        edad = randint(EDAD_MIN,EDAD_MAX)
        correo = f"{nombre.lower()}{apellido.lower()}{choice(dominios_data)}"
        calle = f"Calle: {randint(100,500)} N°: {randint(1100,3000)}"
        localidad = choice(localidades_data)
        provincia = choice(provincias_data)
        sector = choice(sectores_data)

        lista.append(new_empleado(legajo, nombre, apellido, genero, edad, correo, calle,localidad, provincia, sector, lista))


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


#//////////////////////////////////////////////////////////////programacion funcional////////////////////////////////////////////////////////////////////////////////////////



def mapear_lista(procesadora, lista:list) -> list:
    lista_retorno = []
    for el in lista:
        lista_retorno.append(procesadora(el))
    return lista_retorno


def filtra_lista(filtradora, lista: list) -> list:
    lista_filtrada = []
    for el in lista:
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada


def for_each_lista(funcion, lista:list) -> None:
    for i in range(len(lista)):
        lista[i] = funcion(lista[i])


def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)