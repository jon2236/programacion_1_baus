# Ejercicio Nivelación
# Una reconocida productora de contenidos audiovisuales está en busca de nuevas ideas
# para su próximo proyecto, que promete cautivar al público.
# Las posibles temáticas para explorar son las siguientes:
# • Comedia
# • Ciencia ficción
# • Drama
# Para ello, la empresa ha decidido realizar una encuesta entre sus empleados para
# recopilar información valiosa. Los datos para recopilar por cada empleado son los
# siguientes:
# A) Información a ingresar por cada empleado encuestado:
# • Nombre del empleado
# • Edad (debe ser mayor o igual a 18)
# • Género (Masculino - Femenino)
# • Temática de interés (Comedia, Ciencia ficción, Drama)
# B) Se deben cargar 10 encuestas a través de la terminal.
# C) Se requiere determinar:
# • La cantidad de empleados de género masculino que votaron por Ciencia ficción o
# Drama, cuya edad esté entre 25 y 50 años, inclusive.
# • El porcentaje de empleados que no votaron por Comedia, siempre y cuando su
# género no sea Femenino o su edad esté comprendida entre 30 y 40 años.
# • El nombre y la temática de interés votada por el empleado masculino de mayor
# edad.

cantidad_encuestas = 2

contador_masculinos_entre_25_50 = 0
contador_no_votaron_por_comedia_no_femeninos = 0
empleado_masculino_mayor_edad = 0
flag_masculino_mayor_edad = True

def porcentaje(cantidad, total):
    return cantidad * 100 / total
    

for i in range(cantidad_encuestas):

    while True:
        nombre = input("ingrese su nombre")
        if not nombre.isalpha():
            print("eso no es un nombre")
        elif len(nombre) > 15:
            print("nombre demasiado largo")
        elif len(nombre) < 3:
            print("nombre demasiado corto")
        else:
            break

    while True:
        try:
            edad = int(input("ingrese su edad: "))
            if edad >= 18:
                break
            else:
                print("edad invalida")
        except:
            print("esto no es un numero")
    print(edad)

    
    genero = input("ingrese genero")
    while genero != "femenino" and genero != "masculino":
        genero = input("genero invalido, reingrese genero")
    print(genero)


    tematica = input("ingrese tematica")
    while tematica != "comedia" and tematica != "drama" and tematica != "ciencia":
        tematica = input("tematica invalida, reingrese tematica")
    print(tematica)






    if(genero == "masculino" and tematica != "comedia" and (edad >= 25 and edad <= 50)):
        contador_masculinos_entre_25_50 += 1
    

    if(tematica != "comedia" and genero == "masculino" or edad >= 30 and edad <= 40):
        contador_no_votaron_por_comedia_no_femeninos += 1
# • El nombre y la temática de interés votada por el empleado masculino de mayor
# edad.
    if(genero == "masculino" and edad >= empleado_masculino_mayor_edad or flag_masculino_mayor_edad == True):
        empleado_masculino_mayor_edad = edad
        nombre_masculino_mas_viejo = nombre
        tematica_interes_masculino_mas_viejo = tematica
        flag_masculino_mayor_edad = False






#porcentaje_punto_b = contador_no_votaron_por_comedia_no_femeninos * 100 / cantidad_encuestas

resultado = porcentaje(contador_no_votaron_por_comedia_no_femeninos, cantidad_encuestas)

print(f"La cantidad de empleados de género masculino que votaron por Ciencia ficción o Drama, cuya edad esté entre 25 y 50 años, inclusive {contador_masculinos_entre_25_50} ")
print(f"El porcentaje de empleados que no votaron por Comedia, siempre y cuando su género no sea Femenino o su edad esté comprendida entre 30 y 40 años es {resultado}")
print(f"El nombre y la temática de interés votada por el empleado masculino de mayor edad es \n {nombre_masculino_mas_viejo}\n {tematica_interes_masculino_mas_viejo}")