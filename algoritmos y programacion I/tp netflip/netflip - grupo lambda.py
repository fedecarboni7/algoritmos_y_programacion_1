#En proceso...

"""
La aplicación debe tener un menú principal para manejar: 
1.Usuarios 2.Películas 3.Recomendaciones 4.Salir

Ejemplo de menu:
"""

def usuarios():
    return None

def peliculas():
    return None

def recomendaciones():
    return None

def mostrar_menu():
    print(f"\nMenú Principal\n")
    print("1. Usuarios")
    print("2. Películas")
    print("3. Recomendaciones")
    print("4. Salir")
    opcion = int(input(f"\nIngrese una opción: "))
    return opcion

def menu(opcion):
    if(opcion == 1):
        usuarios()
        menu(mostrar_menu())
    elif(opcion == 2):
        peliculas()
        menu(mostrar_menu())
    elif(opcion == 3):
        recomendaciones()
        menu(mostrar_menu())
    elif(opcion != 4):
        print(f"\nIngrese una opción del 1 al 4")
        menu(mostrar_menu())
    return

menu(mostrar_menu())