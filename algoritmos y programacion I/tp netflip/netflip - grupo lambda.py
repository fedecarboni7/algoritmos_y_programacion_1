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

def leer_info_bin(peliculas):
    try:
        linea = pickle.load(peliculas)
        registro = linea
    except EOFError:
        registro = [" "," "," "," "," "] # Condición de salida del while
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
        peliculas(submenu_peliculas(), ruta)
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
        lista_a_archivo(ruta, "usuarios.csv", ordenar(ruta, "usuarios.csv"))
        usuarios(submenu_usuarios(), ruta)
    elif(opcion == 3):
        baja_de_usuario()
        usuarios(submenu_usuarios(), ruta)
    elif(opcion == 4):
        print('\nGenerando lista...\n')
        listar_por_id(ordenar(ruta, "usuarios.csv"))
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
    
    usuarios = open(f'{ruta}usuarios.csv','a')
    
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
                usuarios.write(":{}".format(men[3]))

            clave_anterior = men

            if men == clave_usuario_1:
                clave_usuario_1 = id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_info(usuarios_1)
            elif men == clave_usuario_2:
                clave_usuario_2 = id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_info(usuarios_2)
            elif men == clave_usuario_3:
                clave_usuario_3 = id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_info(usuarios_3)

            men = min(clave_usuario_1, clave_usuario_2, clave_usuario_3)
        
        if usuarios.tell() != 0:
            usuarios.write("\n")

        clave_anterior = men

        usuarios.write("{},{},{},{}".format(clave_anterior[0],clave_anterior[1],clave_anterior[2],clave_anterior[3]))
        
        if men == clave_usuario_1:
            clave_usuario_1 = id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_info(usuarios_1)
        elif men == clave_usuario_2:
            clave_usuario_2 = id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_info(usuarios_2)
        elif men == clave_usuario_3:
            clave_usuario_3 = id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_info(usuarios_3)

    usuarios.write('\n')
    
    usuarios_1.close()
    usuarios_2.close()
    usuarios_3.close()
    usuarios.close()

    os.remove(f"{ruta}usuarios_1.csv")
    os.remove(f"{ruta}usuarios_2.csv")
    os.remove(f"{ruta}usuarios_3.csv")

    if errores:
        print('\nSe encontraron errores en la carga de usuarios, revise "log.txt" para comprobar los usuarios afectados.')
    print('\nMerge de usuarios completado con éxito.\n')

    return

def alta_de_usuario(ruta):
    if not os.path.exists(f"{ruta}usuarios.csv"):
        merge_usuarios(ruta)

    with open(f'{ruta}usuarios.csv','a') as usuarios:
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
            
            usuarios.write(f"{id_usuario},{nombre} {apellido},{año_de_nacimiento},\n")

            seguir = input(f"\n¿Querés seguir creando usuarios? (s/n): ")
    return

def baja_de_usuario():
    lista_usuarios = ordenar(ruta, "usuarios.csv")
    baja_exitosa = False
    print("\n--- Baja de usuario ---")
    id_baja = input('Ingrese el ID de usuario: ')
    for linea in lista_usuarios:
        if id_baja in linea:
            baja_exitosa = True
            lista_usuarios.remove(linea)

    if baja_exitosa:
        lista_a_archivo(ruta, "usuarios.csv", lista_usuarios)
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
    if hay_usuarios(ruta,"usuarios.csv"):
        nombre_mas_largo = max(lista_id_ordenados, key=lambda i: len(i[1]))[1] # Devuelve el nombre más largo de la lista
        print(' Lista de usuarios '.center(31 + max(len(nombre_mas_largo) + 2, 22), '-'))
        print('ID Usuario'.ljust(14) + 'Nombre y Apellido'.ljust(max(len(nombre_mas_largo) + 2, 22)) + 'Año de Nacimiento\n')
        for usuario in lista_id_ordenados:
            id_usuario, nombre, año_de_nacimiento = usuario[0:3]
            print(id_usuario.ljust(14) + nombre.ljust(max(len(nombre_mas_largo) + 2, 22)) + año_de_nacimiento)
    else:
        print("No se encuentran usuarios para listar.")
    return

def lista_a_archivo(ruta, archivo, lista_id_ordenados):
    with open(f'{ruta}{archivo}','w') as usuarios_ordenado:
        for i in range(len(lista_id_ordenados)):
            usuarios_ordenado.write(f"{lista_id_ordenados[i][0]},{lista_id_ordenados[i][1]},{lista_id_ordenados[i][2]},{lista_id_ordenados[i][3]}\n")
    return

def lista_a_archivo_bin(ruta, archivo, lista_peliculas):
    with open(f'{ruta}{archivo}','wb') as peliculas:
        for i in range(len(lista_peliculas)):
            pickle.dump(lista_peliculas[i], peliculas)
    return

def hay_usuarios(ruta, archivo):
    with open(f"{ruta}{archivo}","r") as archivo_usuarios:
        leer_info(archivo_usuarios)
        bool_hay_usuarios = 0 != archivo_usuarios.tell()
    return bool_hay_usuarios
    
def submenu_peliculas():
    print("\n--- Peliculas ---\n")
    print("1. Dar de alta una pelicula")
    print("2. Dar de baja una pelicula")
    print("3. Listar las películas por puntaje")
    print("4. Listar las películas ordenadas por género y por director")
    print("5. Asignar una película a un usuario")
    print("6. Volver al menú principal")
    opcion = int(input(f"\nIngrese una opción: "))
    return opcion

def peliculas(opcion, ruta):
    if(opcion == 1):
        alta_de_pelicula(ruta)
        peliculas(submenu_peliculas(), ruta)
    elif(opcion == 2):
        lista_a_archivo_bin(ruta, "peliculas.txt", baja_de_pelicula(ruta))
        peliculas(submenu_peliculas(), ruta)
    elif(opcion == 3):
        print('\nGenerando lista...\n')
        listar_pelicula_puntaje()
        peliculas(submenu_peliculas(), ruta)
    elif(opcion == 4):
        print('\nGenerando lista...\n')
        listar_pelicula_gen()
        peliculas(submenu_peliculas(), ruta)
    elif(opcion == 5):
        asignar_pelicula_usuario()
        peliculas(submenu_peliculas(), ruta)
    elif(opcion != 6):
        print(f"\nIngrese una opción del 1 al 5")
        peliculas(submenu_peliculas(), ruta)
    return

def alta_de_pelicula(ruta):
    generos = {1:"drama", 2:"comedia", 3:"terror", 4:"suspenso", 5:"accion", 6:"romantica"}
    with open(f'{ruta}peliculas.txt','ab') as archivo_peliculas:
        seguir = "s"
        while seguir == "s":
            print("\n--- Alta de película ---")
            titulo = input(f"Ingrese título: ")
            if titulo[0].islower():
                titulo = titulo.capitalize()
            director_nombre = input(f"Ingrese nombre del director: ")
            if director_nombre[0].islower():
                director_nombre = director_nombre.capitalize()
            director_apellido = input(f"Ingrese apellido del director: ")
            if director_apellido[0].islower():
                director_apellido = director_apellido.capitalize()
            director = director_nombre + director_apellido
            print("Elija el genero:")
            print("1. Drama")
            print("2. Comedia")
            print("3. Terror")
            print("4. Suspenso")
            print("5. Acción")
            print("6. Romantica")
            opcion = int(input("\nIngrese genero: "))
            genero = generos[opcion]
            puntaje = int(input("Ingrese puntaje del 1 al 9: "))

            id_pelicula = str(hash(titulo) % (10 ** 8))
            
            pelicula = [id_pelicula, titulo, director, genero, puntaje]
            pickle.dump(pelicula, archivo_peliculas)
            
            print(f"\nPelicula cargada con éxito. ID de pelicula: {id_pelicula}")
            seguir = input(f"\n¿Querés seguir cargando peliculas? (s/n): ")
    return

def baja_de_pelicula(ruta):
    with open(f'{ruta}peliculas.txt','r+b') as archivo_peliculas:
        lista_peliculas = []
        while [" "," "," "," "," "] not in lista_peliculas:
            lista_peliculas += [leer_info_bin(archivo_peliculas)]

        print("\n--- Baja de pelicula ---")
        id_baja = input('Ingrese el ID de pelicula: ')
        baja_exitosa = False     
        for linea in lista_peliculas:
            if id_baja == linea[0]:
                baja_exitosa = True
                lista_peliculas.remove(linea)
        if baja_exitosa:
            print(f'\nPelicula {id_baja} dado de baja con éxito.\n')
        else:
            print(f'\nLa pelicula {id_baja} no existe en la base de datos.\n')
            
    return lista_peliculas

def listar_pelicula_puntaje():
    return None

def listar_pelicula_gen():
    return None

def asignar_pelicula_usuario():
    return None

def recomendaciones():
    return None

#------- Bloque de inicio -------#
if not os.path.exists(f"{ruta}usuarios_1.csv") and not os.path.exists(f"{ruta}usuarios.csv"):
    usuarios = open(f"{ruta}usuarios.csv", "w")
    usuarios.close()
menu(mostrar_menu(), ruta)
