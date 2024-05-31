from random import randint

def mostrar_lista(lista:list) -> None:
    for el in lista:
        print(el, end = " ")
    print()


def validar_lista(lista:list) -> bool:
    if isinstance(lista, list):
        raise TypeError("se esperaba una lista")
    return True


def cargar_lista_random(lista:list, size:int, desde:int, hasta:int) -> None:
    from random import randint
    for _ in range(size):
        lista.append(randint(desde, hasta))


def crear_lista_enteros(size:int, min:int, max:int) -> list:
    from random import randint
    lista = []
    for _ in range(size):
        lista.append(randint(min, max))
    return lista


def totalizar_lista(lista:list) -> int:
    total = 0
    for valor in (lista):
        total += valor
    return total


def calcular_promedio(lista:list) -> float:
    if isinstance(lista, list):
        suma = len(lista)
        if suma == 0:
            raise ValueError("no esta definido el promedio de una lista vacia")
        return totalizar_lista(lista) / suma
    

def calcular_promedioab(a:int, b:int) -> float:
    return (a + b) / 2


def calcular_mayor(lista:list) -> int:
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("no esta definido el mayor de una lista vacia")
        flag_mayor = True
        for el in lista:
            if flag_mayor == True or el > num_mayor:
                num_mayor = el
                flag_mayor = False
    return num_mayor


def calcular_menor(lista:list) -> int:
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("no esta definido el menor de una lista vacia")
        flag_menor = True
        for el in lista:
            if flag_menor == True or el < num_menor:
                num_menor = el
                flag_menor = False
    return num_menor


def entero_in_lista(lista: list, target:int) -> bool:
    entero = False
    for el in lista:
        if target == el:
            entero = True
            break
    return entero


def numeros_pares(lista: list) -> list:
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("")
    pares = [num for num in lista if num % 2 == 0]
    return pares


def buscar_en_lista(lista:list, target:int) -> int:
    indice = -1
    for i in range(len(lista)):
        if lista[i] == target:
            indice = i
            break
    return indice


def contar_en_lista(lista:list, target:int) -> int:
    contador = 0
    for elem in lista:
        if elem == target:
            contador += 1
    return contador


def ordenar_lista_ascendente(lista:list) -> None:
    size = len(lista)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def ordenar_lista_descendente(lista:list) -> None:
    size = len(lista)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


def ordenador_listas(lista:list, ascendente:bool = True) -> None:
    if isinstance(lista,list):
        size = len(lista)
        if size == 0:
            raise ValueError("se espera algun objeto en lista")
    else:
        raise TypeError("se espera una lista")
    for i in range(size - 1):
        for j in range(i + 1, size):
            if ascendente:
                if lista[i] > lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else:
                if lista[i] < lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux


def swap_lista(lista:list, i:int, j:int) -> None:
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux




def validar_legajo(min_leg:int, max_leg:int, legajo:int, lista:list):
    """_summary_
    esta funcion genera legajos

    Args:
        min_leg (int): _description_
        valor minimo admitido
        max_leg (int): _description_
        valor maximo admitido
        lista (list): _description_
        lista destino
    """
    if legajo == None and legajo == "" and legajo == 0:
        while True:
            aux = input("ingrese legajo, entre 20.000 y 30.000 inclusive")
            for i in range(len(lista)):
                if lista[i]["legajo"] != aux and aux.isdigit():
                    aux = int(aux)
                    if aux >= min_leg and aux <= max_leg:
                        return aux
                    else:
                        print("ERROR: El legajo debe estar entre 20000 y 30000 inclusive")
                else:
                    print("ERROR: El legajo ya existe")
    else:
        if legajo >= min_leg and legajo <= max_leg:
            return legajo
        else:
            print("ERROR: El legajo debe estar entre 20000 y 30000 inclusive")


def validar_nombre(min_caract:int, max_caract:int, lista:list):
    """_summary_
    esto es una funcion q validad nombres

    Args:
        min_caract (int): _description_
        valor minimo admitido
        max_caract (int): _description_
        valor maximo admitido
        lista (list): _description_
        lista destino
    """
    while True:
        aux = input("ingrese nombre: ")
        if aux.isalpha():
            if len(aux) > min_caract and len(aux) <= max_caract:
                lista.append(aux)
                return
            else:
                print("ERROR: caracteres fuera de parametros, re ingrese su nombre con mas de tres letras y menos de 15")
        else:
            print("error, el nombre no puede tener numeros. Re ingrese su nombre con no menos de 3 letras y no mas de 15")


def validar_genero(lista:list):
    while True:
        aux = input("ingrese genero: M or F. ").lower()
        if aux == "m" or aux == "f":
            lista.append(aux)
            break
        else:
            print("error: la entrada debe ser f or m")

def validar_notas(nota_max:int, nota_min:int,  nro_parcial:int, lista:list):
    while True:
        aux = (input(f"ingrese nota parcial {nro_parcial}, entre 0 y 10: "))
        if aux.isdigit():
            aux = int(aux)
            if aux >= nota_min and aux <= nota_max:
                lista.append(aux)
                break
            else:
                print("error: fuera de rango")
        else:
            print("error: se esperaba un numero")


def promediar_notas_alumnos(valor_a:int, valor_b:int, lista_promedios:list) -> None:
    promedio = calcular_promedioab(valor_a, valor_b)
    lista_promedios.append(promedio)


def cargar_alumno_nuevo(lista:list, TAM):
    for _ in range(TAM):
        nuevo_alumno = []
        min_leg = 20000
        max_leg = 30000

        validar_legajo(min_leg, max_leg, nuevo_alumno)
        validar_nombre(3, 15, nuevo_alumno)
        validar_genero(nuevo_alumno)
        validar_notas(10, 0, 1, nuevo_alumno)
        validar_notas(10, 0, 2, nuevo_alumno)
        promediar_notas_alumnos(nuevo_alumno[3], nuevo_alumno[4], nuevo_alumno)

        lista.append(nuevo_alumno)