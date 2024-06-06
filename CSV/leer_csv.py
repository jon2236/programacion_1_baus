def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

with open(get_path_actual("personas.csv")) as archivo:
    encabezzado = archivo.readline()
    
    for linea in archivo.readlines():
        
        print(linea)


