from os import system

def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")

def menu() -> str:
    limpiar_pantalla()
    print("      menu de opciones")
    print("1- saludar")
    print("2- brindar")
    print("3- despedir")
    print("4- fin del programa")

    return input("ingrese opcion")

def saludar() -> str:
    print("hola")

def brindar() -> str:
    print("skål")

def despedir() -> str:
    print("bye")




flag_saludo = False
flag_brindar = False

while True:
    match menu():
        case "1":
            saludar()
            flag_saludo = True
        case "2":
            if(flag_saludo == True):
                brindar()
                flag_brindar = True
            else:
                print("no hola, no skål")
        case "3":
            if(flag_saludo == True and flag_brindar == True):
                despedir()
            else:
                print("no nos vayamos sin saludar y brindar")
            flag_saludo = False
            flag_brindar = False
        case "4":
            question = input("realmente desea salir? s/n")
            if(question == "s"):
                break
    pausar()

print("fin del programa")