
with open("./archivos/ejemplo2.csv", "r", encoding = "utf-8") as archivo:
    for linea in archivo.readlines():
        dato = linea.strip("\n")
        print(dato)

