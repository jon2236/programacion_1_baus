from listas_paralelass_dicc import *
from funciones_listas_dicc import *

TAM = 2
alumnos = []

for _ in range(TAM):
    legajo = validar_legajo(20000, 30000, alumno)
    nombre = validar_nombre(3, 15)
    genero = validar_genero(alumno)
    nota_1 = validar_notas(10, 0, 1, alumno)
    nota_2 = validar_notas(10, 0, 2, alumno)
    alumnos.append(alumno)
    alumno.append(calcular_promedioab(alumno[3], alumno[4]))
mostrar_alumnos(alumnos)





# alumno = []
#     legajo = validar_legajo(20000, 30000, alumno)
#     nombre = validar_nombre(3, 15, alumno)
#     genero = validar_genero(alumno)
#     nota_1 = validar_notas(10, 0, 1, alumno)
#     nota_2 = validar_notas(10, 0, 2, alumno)
#     alumnos.append(alumno)
#     alumno.append(calcular_promedioab(alumno[3], alumno[4]))
# mostrar_alumnos(alumnos)



#     alumno = []
#     validar_legajo(20000, 30000, alumno)
#     validar_nombre(3, 15, alumno)
#     validar_genero(alumno)
#     validar_notas(10, 0, 1, alumno)
#     validar_notas(10, 0, 2, alumno)
#     promediar_notas_alumnos(alumno[3], alumno[4], alumno)
#     print(alumno)
#     alumnos.append(alumno)
# mostrar_alumnos(alumnos)