import pickle
import pathlib
import os

ruta = str(pathlib.Path(__file__).parent.absolute()) + '\\archivos\\' 

def leer_info(usuario):
    linea = usuario.readline()
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        registro = ['999zz99','','',''] # Condición de salida del while
    return registro

def mostrar_menu():
    print(f"\n--- Menú Principal ---\n")
    print("1. Usuarios")
    print("2. Películas")
    print("3. Recomendaciones")
    print("4. Salir")
    opcion = int(input(f"\nIngrese una opción: "))
    return opcion

def menu(opcion, ruta):
    if(opcion == 1):
        usuarios(submenu_usuarios(), ruta)
        menu(mostrar_menu(), ruta)
    elif(opcion == 2):
        peliculas()
        menu(mostrar_menu(), ruta)
    elif(opcion == 3):
        recomendaciones()
        menu(mostrar_menu(), ruta)
    elif(opcion != 4):
        print(f"\nIngrese una opción del 1 al 4")
        menu(mostrar_menu(), ruta)
    return

def submenu_usuarios():
    print("\n--- Usuarios ---\n")
    print("1. Merge de usuarios")
    print("2. Dar de alta un usuario")
    print("3. Dar de baja un usuario")
    print("4. Listar usuarios por ID")
    print("5. Volver al menú principal")
    opcion = int(input(f"\nIngrese una opción: "))
    return opcion

def usuarios(opcion, ruta):
    if(opcion == 1):
        merge_usuarios(ruta)
        usuarios(submenu_usuarios(), ruta)
    elif(opcion == 2):
        alta_de_usuario(ruta)
        lista_a_archivo(ruta, "usuarios_merge.csv", ordenar(ruta, "usuarios_merge.csv"))
        usuarios(submenu_usuarios(), ruta)
    elif(opcion == 3):
        baja_de_usuario()
        usuarios(submenu_usuarios(), ruta)
    elif(opcion == 4):
        print('\nGenerando lista...\n')
        listar_por_id(ordenar(ruta, "usuarios_merge.csv"))
        usuarios(submenu_usuarios(), ruta)
    elif(opcion != 5):
        print(f"\nIngrese una opción del 1 al 5")
        usuarios(submenu_usuarios(), ruta)
    return

def merge_usuarios(ruta):
    errores = False
    try:
        lista_a_archivo(ruta, "usuarios_1.csv", ordenar(ruta, "usuarios_1.csv"))
        usuarios_1 = open(f'{ruta}usuarios_1.csv','r')
        lista_a_archivo(ruta, "usuarios_2.csv", ordenar(ruta, "usuarios_2.csv"))
        usuarios_2 = open(f'{ruta}usuarios_2.csv','r')
        lista_a_archivo(ruta, "usuarios_3.csv", ordenar(ruta, "usuarios_3.csv"))
        usuarios_3 = open(f'{ruta}usuarios_3.csv','r')
    except FileNotFoundError:
        return print("\nNo hay archivos de usuarios suficientes para generar un merge.\nPor favor elija otra opción.")
    
    usuarios_merge = open(f'{ruta}usuarios_merge.csv','a')
    
    id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_info(usuarios_1)
    clave_usuario_1 =[id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1]
    
    id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_info(usuarios_2)
    clave_usuario_2 = [id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2]

    id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_info(usuarios_3)
    clave_usuario_3 = [id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3]

    max = "999zz99" # Valor ajustado para que coincida con el formato de id_usuario
    clave_anterior = [" "," "," "," "]

    while id_usuario_1 != max or id_usuario_2 != max or id_usuario_3 != max:

        men = min(clave_usuario_1, clave_usuario_2, clave_usuario_3)
        
        while men[0] == clave_anterior[0]:
            if men[1] != clave_anterior[1] or men[2] != clave_anterior[2]:
                errores = True
                try:
                    log_error = open(f'{ruta}log.txt','a')
                except FileNotFoundError:
                    log_error = open(f'{ruta}log.txt','w+')
                id_usuario_error, nombre_error, año_nacimiento_error, peliculas_error = men
                log_error.write(f'{id_usuario_error},{nombre_error},{año_nacimiento_error},{peliculas_error}\n')
                log_error.close()
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

    usuarios_merge.write('\n')
    
    usuarios_1.close()
    usuarios_2.close()
    usuarios_3.close()
    usuarios_merge.close()

    os.remove(f"{ruta}usuarios_1.csv")
    os.remove(f"{ruta}usuarios_2.csv")
    os.remove(f"{ruta}usuarios_3.csv")

    if errores:
        print('\nSe encontraron errores en la carga de usuarios, revise "log.txt" para comprobar los usuarios afectados.')
    print('\nMerge de usuarios completado con éxito.\n')

    return

def alta_de_usuario(ruta):
    if not os.path.exists(f"{ruta}usuarios_merge.csv"):
        merge_usuarios(ruta)

    with open(f'{ruta}usuarios_merge.csv','a') as usuarios_merge:
        seguir = "s"
        while seguir == "s":
            print("\n--- Creación de usuario ---")
            nombre = input(f"Ingrese nombre: ")
            if nombre[0].islower():
                nombre = nombre.capitalize()
            apellido = input(f"Ingrese apellido: ")
            if apellido[0].islower():
                apellido = apellido.capitalize()
            año_de_nacimiento = input(f"Ingrese año de nacimiento: ")
            prefijo_id = str(hash(nombre + apellido) % (10 ** 3))
            id_usuario = prefijo_id + nombre[0] + apellido[0] + año_de_nacimiento[2:4]
            
            print(f"\nUsuario creado con éxito. Tu ID es: {id_usuario}")
            
            usuarios_merge.write(f"{id_usuario},{nombre} {apellido},{año_de_nacimiento},\n")

            seguir = input(f"\n¿Querés seguir creando usuarios? (s/n): ")
    return

def baja_de_usuario():
    with open(f'{ruta}usuarios_merge.csv', 'r+') as usuarios_merge:
        baja_exitosa = False
        print("\n--- Baja de usuario ---")
        id_baja = input('Ingrese el ID de usuario: ')
        lista_usuarios = usuarios_merge.readlines()
        for linea in lista_usuarios:
            if id_baja in linea:
                baja_exitosa = True
                lista_usuarios.remove(linea)
        usuarios_merge.truncate(0)
        usuarios_merge.seek(0)
        usuarios_merge.writelines(lista_usuarios)

        if baja_exitosa:
            print(f'\nUsuario {id_baja} dado de baja con éxito.\n')
        else:
            print(f'\nEl usuario {id_baja} no existe en la base de datos.\n')
    return

def ordenar(ruta, archivo):
    with open(f'{ruta}{archivo}','r+') as usuarios_ordenado:
        max = "999zz99"
        lista_id_ordenados = []

        id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas = leer_info(usuarios_ordenado)
        clave_usuario = [id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas]
        
        while id_usuario != max:
            lista_id_ordenados += [clave_usuario]
            id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas = leer_info(usuarios_ordenado)
            clave_usuario = [id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas]

    lista_id_ordenados.sort(key=lambda i: i[0])
    
    return lista_id_ordenados

def listar_por_id(lista_id_ordenados):
    nombre_mas_largo = max(lista_id_ordenados, key=lambda i: len(i[1]))[1] # Devuelve el nombre más largo de la lista
    print(' Lista de usuarios '.center(31 + max(len(nombre_mas_largo) + 2, 22), '-'))
    print('ID Usuario'.ljust(14) + 'Nombre y Apellido'.ljust(max(len(nombre_mas_largo) + 2, 22)) + 'Año de Nacimiento\n')
    for usuario in lista_id_ordenados:
        id_usuario, nombre, año_de_nacimiento = usuario[0:3]
        print(id_usuario.ljust(14) + nombre.ljust(max(len(nombre_mas_largo) + 2, 22)) + año_de_nacimiento)
    return

def lista_a_archivo(ruta, archivo, lista_id_ordenados):
    with open(f'{ruta}{archivo}','w') as usuarios_ordenado:
        
        for i in range(len(lista_id_ordenados)):
            usuarios_ordenado.write(f"{lista_id_ordenados[i][0]},{lista_id_ordenados[i][1]},{lista_id_ordenados[i][2]},{lista_id_ordenados[i][3]}\n")
    return

def hay_usuarios(archivo_usuarios):
    leer_info(archivo_usuarios)
    hay_usuarios = 0 != archivo_usuarios.tell()
    archivo_usuarios.seek(0)
    return hay_usuarios
    
def peliculas():
    return None

def recomendaciones():
    return None

#------- Bloque de inicio -------#
if not os.path.exists(f"{ruta}usuarios_1.csv") and not os.path.exists(f"{ruta}usuarios_merge.csv"):
    usuarios_merge = open(f"{ruta}usuarios_merge.csv", "w")
    usuarios_merge.close()
menu(mostrar_menu(), ruta)
