#REVISAAAR
import raiz_cuadrada
import funcion_division


def mostrar_menu():
    print("1. Cálculo de raiz")
    print("2. Cálculo de división")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion


def menu(opcion):
    mostrar_menu()
    while(opcion != 3):
        if(opcion == 1):
            raiz_cuadrada.main()
        elif(opcion == 2):
            funcion_division.main()
        menu(opcion)
    return


menu(mostrar_menu())