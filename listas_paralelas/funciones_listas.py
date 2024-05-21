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

    