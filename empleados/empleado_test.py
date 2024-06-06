from funciones_empleados_paralelas import *



numeros = [3, 45, 2, 66, 10, 30, 42, 66]



x = filtra_lista(lambda numero : numero % 2 != 0, numeros)
print(x)








# tam = 1
# test = []
# cargar_empleados(test,10)
# mostrar_empleados(test)

# def cargar_lista_manual(lista:list, tam:int):
#     for _ in range(tam):
#         legajo = validar_legajo(20000, 30000, 0, lista)
#         nombre = "jona"
#         apellidos = "sdf"
#         genero = "m"
#         edad = 45
#         correo = "sfhsoffjspf@idjgrg"
#         calle = "sdgjrg"
#         localidad = "sdkfef"
#         provincia = "sjkghsjklg"
#         sector = "gfkgkdhrgkj"
        
#         new_empleado(legajo,nombre, apellidos, genero, edad, correo, calle, localidad, provincia, sector, lista)
        
# cargar_lista_manual(test, tam)