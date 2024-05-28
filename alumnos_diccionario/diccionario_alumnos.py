from listas_paralelass_dicc import *
from funciones_listas_dicc import *

TAM = 1
alumnos = []

for _ in range(TAM):
    alumno = []
    validar_legajo(20000, 30000, alumno)
    validar_nombre(3, 15, alumno)
    validar_genero(alumno)
    validar_notas(10, 0, 1, alumno)
    validar_notas(10, 0, 2, alumno)
    promediar_notas_alumnos(alumno[3], alumno[4], alumno)
    print(alumno)
    alumnos.append(alumno)
mostrar_alumnos(alumnos)