import raiz_cuadrada
import funcion_division


def mostrar_menu():
    print("")
    print("1. Cálculo de raiz")
    print("2. Cálculo de división")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion


def menu(opcion):
    if(opcion == 1):
        raiz_cuadrada.main()
        menu(mostrar_menu())
    elif(opcion == 2):
        funcion_division.main()
        menu(mostrar_menu())
    return


menu(mostrar_menu())
