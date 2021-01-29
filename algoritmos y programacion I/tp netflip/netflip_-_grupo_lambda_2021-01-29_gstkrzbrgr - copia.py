import pickle
import pathlib # Necesario para obtener la ruta del programa

def mostrar_menu():
    print("\nMenú Principal\n")
    print("1. Usuarios")
    print("2. Películas")
    print("3. Recomendaciones")
    print("4. Salir")
    opcion = int(input("\nIngrese una opción: "))
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
        print("\nIngrese una opción del 1 al 4")
        menu(mostrar_menu())
    return

def leer_info(usuario):
    linea = usuario.readline()
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        registro = ['999999','','',''] # Condición de salida del while
    return registro

def usuarios():
    
    ruta = pathlib.Path(__file__).parent.absolute() # Devuelve la ruta de la carpeta donde se ejecuta el programa
    
    try:
#         ordenar("usuarios_1.csv") # Debe llamarse después de abrir el archivo
        usuarios_1 = open(f'{ruta}\\usuarios_1.csv','r') # Agregado '\\' para que el programa encuentre el archivo
    except FileNotFoundError: # io.UnsupportedOperation ocurre cuando se trata de usar readline en un archivo abierto en modo 'w', se resuelve abriendo el archivo como 'r+'
        usuarios_1 = open(f'{ruta}\\usuarios_1.csv','r+')
    try:
#         ordenar("usuarios_2.csv") # Debe llamarse después de abrir el archivo
        usuarios_2 = open(f'{ruta}\\usuarios_2.csv','r')
    except FileNotFoundError:
        usuarios_2 = open(f'{ruta}\\usuarios_2.csv','r+')
    try:
#         ordenar("usuarios_3.csv") # Debe llamarse después de abrir el archivo
        usuarios_3 = open(f'{ruta}\\usuarios_3.csv','r')
    except FileNotFoundError:
        usuarios_3 = open(f'{ruta}\\usuarios_3.csv','r+')
    
    usuarios_merge = open(f'{ruta}\\usuarios_merge.csv','r+')

    csv_error = open(f'{ruta}\\log.csv','r+')

    id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_info(usuarios_1)
    clave_usuario_1 =[id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1]
    
    id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_info(usuarios_2)
    clave_usuario_2 = [id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2]

    id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_info(usuarios_3)
    clave_usuario_3 = [id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3]

    max = "999999"
    clave_anterior = [" "," "," "," "]

    while id_usuario_1 != max or id_usuario_2 != max or id_usuario_3 != max:

        men = min(clave_usuario_1, clave_usuario_2, clave_usuario_3)
        
        while men[0] == clave_anterior[0]:
            if men[1] != clave_anterior[1] or men[2] != clave_anterior[2]:
                csv_error.write(f"Las claves {men} y {clave_anterior} no coinciden\n")
            else:
                usuarios_merge.write(":{}".format(men[3]))

            clave_anterior = men

            if men == clave_usuario_1:
                clave_usuario_1 = id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_info(usuarios_1)
            elif men == clave_usuario_2:
                clave_usuario_2 = id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_info(usuarios_2)
            elif men == clave_usuario_3:
                clave_usuario_3 = id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_info(usuarios_3)

            men = min(clave_usuario_1, clave_usuario_2, clave_usuario_3)
        
        if usuarios_merge.tell() != 0:
            usuarios_merge.write("\n")

        clave_anterior = men
                
        usuarios_merge.write("{},{},{},{}".format(clave_anterior[0],clave_anterior[1],clave_anterior[2],clave_anterior[3]))
        
        if men == clave_usuario_1:
            clave_usuario_1 = id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_info(usuarios_1)
        elif men == clave_usuario_2:
            clave_usuario_2 = id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_info(usuarios_2)
        elif men == clave_usuario_3:
            clave_usuario_3 = id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_info(usuarios_3)

    usuarios_1.close()
    usuarios_2.close()
    usuarios_3.close()
    usuarios_merge.close()
    csv_error.close()

    return

def ordenar(archivo):

    ruta = pathlib.Path(__file__).parent.absolute()

    usuarios_ordenado = open(f'{ruta}\\{archivo}','r+')
    
    max = "999999"
    lista = []

    id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas = leer_info(usuarios_ordenado)
    clave_usuario = [id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas]
    
    while id_usuario != max:
        lista += [clave_usuario]
        id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas = leer_info(usuarios_ordenado)
        clave_usuario = [id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas]

    lista.sort(key=lambda i: i[0])
    usuarios_ordenado.seek(0)
    
    for i in range(len(lista)):
        usuarios_ordenado.write(f"{lista[i][0]},{lista[i][1]},{lista[i][2]},{lista[i][3]}\n")

    usuarios_ordenado.close()

    return

def peliculas():
    return None

def recomendaciones():
    return None


menu(mostrar_menu())