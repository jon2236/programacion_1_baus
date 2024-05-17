from funciones.operaciones import *


flag_num1 = False
flag_num2 = False
valor_1 = 0
valor_2 = 0
resultado = 0

while True:

    match menu():
        case "a":
            valor_1 = ingrese_operando("ingrese por favor su primer operando ")
            flag_num1 = True
            print(valor_1)
        case "b":
            if(flag_num1 == False):
                print("ingrese su primer operando antes de ingresar el segundo ")
            else:
                valor_2 =ingrese_operando("ingrese por favor su segundo operando")
                flag_num2 = True
        case "c":
                match sub_menu():
                    case "1":
                        resultado = sumar(valor_1, valor_2)
                        operacion = "la suma de sus operadores "
                    case "2":
                        resultado = restar(valor_1, valor_2)
                        operacion = "la resta de sus operadores "
                    case "3":
                        resultado = multiplicar(valor_1, valor_2)
                        operacion = "la multiplicacion de sus operadores "
                    case "4":
                        if(valor_1 == 0 or valor_2 == 0):
                            print("no se puede dividir por 0")
                        else:
                            resultado = dividir(valor_1, valor_2)
                            operacion = "la division de sus operadores "
                    case "5":
                        if(flag_num2 == True):
                            print("factorial solo necesita 1 valor. solo ingrese el primer operando")
                            break
                        else:
                            resultado = factorial(valor_1)
                            operacion = "el factorial de su operador "
        case "d":
            print(f"el resultado de {operacion} es: {resultado}")
        case "e":
            break
    
    
    
    
    pausar()


print("fin del programa")