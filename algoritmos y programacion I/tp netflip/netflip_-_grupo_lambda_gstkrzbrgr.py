import pickle
import pathlib
import os

'''
Los archivos de usuarios y películas están definidos como variables globales,
así ya no hace falta pasar la variable 'ruta' a todas las funciones (merge
sigue usando 'ruta' como argumento para poder trabajar con los archivos de
entrada (usuarios_1, usuarios_2 y usuarios_3)).
'''
ruta = str(pathlib.Path(__file__).parent.absolute()) + '\\archivos\\' 
archivo_usuarios = ruta + 'usuarios.csv'
archivo_peliculas = ruta + 'peliculas.dat'
MAX_ID_USUARIO = '999zz99' # definido como global, renombrado para evitar errores (max es palabra reservada de Python)

def leer_archivo(archivo):
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        registro = [MAX_ID_USUARIO,'','',''] # Condición de salida del while
    return registro

'''
Esta función fue reemplazada con binario_a_lista() y ya no es necesaria. 
'''
# def leer_archivo_bin(peliculas):
#     try:
#         linea = pickle.load(peliculas)
#         registro = linea
#     except EOFError:
#         registro = [" "," "," "," "," "] # Condición de salida del while
#     return registro

def pantalla_en_espera(texto = ''):
    '''
    Función agregada para que el usuario lea los mensajes que devuelve el
    programa, antes de que aparezcan los submenúes.
    '''
    if texto != '':
        print(texto)
    input('\nPresione una tecla para continuar.')
    return

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
        alta_de_usuario()
        lista_a_archivo(archivo_usuarios, ordenar(archivo_usuarios))
        usuarios(submenu_usuarios(), ruta)
    elif(opcion == 3):
        baja_de_usuario()
        usuarios(submenu_usuarios(), ruta)
    elif(opcion == 4):
        print('\nGenerando lista...\n')
        listar_por_id(ordenar(archivo_usuarios))
        usuarios(submenu_usuarios(), ruta)
    elif(opcion != 5):
        print(f"\nIngrese una opción del 1 al 5")
        usuarios(submenu_usuarios(), ruta)
    return

def merge_usuarios(ruta):
    errores = False
    try:
#         lista_a_archivo(ruta, "usuarios_1.csv", ordenar(ruta, "usuarios_1.csv"))
        usuarios_1 = open(f'{ruta}usuarios_1.csv','r')
#         lista_a_archivo(ruta, "usuarios_2.csv", ordenar(ruta, "usuarios_2.csv"))
        usuarios_2 = open(f'{ruta}usuarios_2.csv','r')
#         lista_a_archivo(ruta, "usuarios_3.csv", ordenar(ruta, "usuarios_3.csv"))
        usuarios_3 = open(f'{ruta}usuarios_3.csv','r')
    except FileNotFoundError:
        return pantalla_en_espera("\nNo hay archivos de usuarios suficientes para generar un merge.\nPor favor elija otra opción.")
    
    usuarios = open(archivo_usuarios,'a')
    
    id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_archivo(usuarios_1)
    clave_usuario_1 =[id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1]
    
    id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_archivo(usuarios_2)
    clave_usuario_2 = [id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2]

    id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_archivo(usuarios_3)
    clave_usuario_3 = [id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3]

    clave_anterior = [" "," "," "," "]

    while id_usuario_1 != MAX_ID_USUARIO or id_usuario_2 != MAX_ID_USUARIO or id_usuario_3 != MAX_ID_USUARIO:

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
                clave_usuario_1 = id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_archivo(usuarios_1)
            elif men == clave_usuario_2:
                clave_usuario_2 = id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_archivo(usuarios_2)
            elif men == clave_usuario_3:
                clave_usuario_3 = id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_archivo(usuarios_3)

            men = min(clave_usuario_1, clave_usuario_2, clave_usuario_3)
        
        if usuarios.tell() != 0:
            usuarios.write("\n")

        clave_anterior = men

        usuarios.write("{},{},{},{}".format(clave_anterior[0],clave_anterior[1],clave_anterior[2],clave_anterior[3]))
        
        if men == clave_usuario_1:
            clave_usuario_1 = id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_archivo(usuarios_1)
        elif men == clave_usuario_2:
            clave_usuario_2 = id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_archivo(usuarios_2)
        elif men == clave_usuario_3:
            clave_usuario_3 = id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_archivo(usuarios_3)

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
    pantalla_en_espera('\nMerge de usuarios completado con éxito.\n')

    return

def alta_de_usuario():
    if not os.path.exists(archivo_usuarios):
        merge_usuarios(ruta)

    with open(archivo_usuarios,'a') as usuarios:
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
            if len(prefijo_id) < 3:
                prefijo_id = prefijo_id.zfill(3)
            id_usuario = prefijo_id + nombre[0] + apellido[0] + año_de_nacimiento[2:4]
            usuarios.write(f"{id_usuario},{nombre} {apellido},{año_de_nacimiento},\n")
            
            print(f"\nUsuario creado con éxito.")
            print(f'ID de Usuario: {id_usuario}')
            print(f'Nombre y Apellido: {nombre} {apellido}')
            print(f'Año de nacimiento: {año_de_nacimiento}')
            
            seguir = input(f"\n¿Querés seguir creando usuarios? (s/n): ")
    return

def baja_de_usuario():
    lista_usuarios = ordenar(archivo_usuarios)
    baja_exitosa = False
    print("\n--- Baja de usuario ---")
    id_baja = input('Ingrese el ID de usuario: ')
    for linea in lista_usuarios:
        if id_baja in linea:
            nombre_usuario = linea[1]
            baja_exitosa = True
            lista_usuarios.remove(linea)

    if baja_exitosa:
        lista_a_archivo(archivo_usuarios, lista_usuarios)
        pantalla_en_espera(f'\nUsuario "{nombre_usuario}" ({id_baja}) dado de baja con éxito.\n')
    else:
        pantalla_en_espera(f'\nEl usuario {id_baja} no existe en la base de datos.\n')
    return

def ordenar(archivo):
    if not os.path.exists(archivo):
        nombre_archivo = archivo.split('\\')[-1]
        print(f'ERROR: El archivo {nombre_archivo} no existe, por favor elija otra opción.\n')
        lista_id_ordenados = []
    else:
        with open(archivo,'r+') as usuarios_ordenado:
            lista_id_ordenados = []

            id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas = leer_archivo(usuarios_ordenado)
            clave_usuario = [id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas]
            
            while id_usuario != MAX_ID_USUARIO:
                lista_id_ordenados += [clave_usuario]
                id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas = leer_archivo(usuarios_ordenado)
                clave_usuario = [id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas]

        lista_id_ordenados.sort(key=lambda i: i[0])
    
    return lista_id_ordenados

def listar_por_id(lista_id_ordenados):
    if lista_id_ordenados != []: # Si la lista está vacía devuelve mensaje de error
        nombre_mas_largo = max(lista_id_ordenados, key=lambda i: len(i[1]))[1] # Devuelve el nombre más largo de la lista
        print(' Lista de usuarios '.center(31 + max(len(nombre_mas_largo) + 2, 22), '-'))
        print('ID Usuario'.ljust(14) + 'Nombre y Apellido'.ljust(max(len(nombre_mas_largo) + 2, 22)) + 'Año de Nacimiento\n')
        for usuario in lista_id_ordenados:
            id_usuario, nombre, año_de_nacimiento = usuario[0:3]
            print(id_usuario.ljust(14) + nombre.ljust(max(len(nombre_mas_largo) + 2, 22)) + año_de_nacimiento)
        pantalla_en_espera()
    else:
        pantalla_en_espera("No se encuentran usuarios para listar.")
    return

def lista_a_archivo(archivo_usuarios, lista_id_ordenados):
    with open(archivo_usuarios,'w') as usuarios_ordenado:
        for i in range(len(lista_id_ordenados)):
            usuarios_ordenado.write(f"{lista_id_ordenados[i][0]},{lista_id_ordenados[i][1]},{lista_id_ordenados[i][2]},{lista_id_ordenados[i][3]}\n")
    return

'''
Como el archivo de películas ahora guarda una lista anidada (una lista de
listas de películas), se simplificó la función y se agregó otra para cargar
datos desde el mismo archivo.
'''
def lista_a_binario(archivo, lista):
    with open(archivo,'wb') as binario:
        pickle.dump(lista, binario)
    return

def binario_a_lista(archivo):
    with open(archivo, 'rb') as binario:
        lista = pickle.load(binario)
    return lista

def hay_usuarios(archivo_usuarios):
    with open(archivo_usuarios,"r") as usuarios:
        leer_archivo(usuarios)
        bool_hay_usuarios = 0 != usuarios.tell()
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
        alta_de_pelicula()
        peliculas(submenu_peliculas(), ruta)
    elif(opcion == 2):
        baja_de_pelicula()
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

def alta_de_pelicula():
    '''
    La función ahora guarda las peliculas en una sola lista para facilitar la
    lectura del archivo (sólo hace falta llamar a pickle.load() una sola vez
    para cargar las películas).
    '''
    generos = {1:"drama", 2:"comedia", 3:"terror", 4:"suspenso", 5:"accion", 6:"romantica"}
    seguir = "s"
    lista_peliculas = binario_a_lista(archivo_peliculas)
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
        director = director_apellido + ', ' + director_nombre
        print("Elija el genero:")
        print("1. Drama")
        print("2. Comedia")
        print("3. Terror")
        print("4. Suspenso")
        print("5. Acción")
        print("6. Romantica")
        opcion = int(input("\nIngrese genero: "))
        tupla_genero = (opcion, generos[opcion])
        puntaje = int(input("Ingrese puntaje del 1 al 9: "))

        id_pelicula = str(hash(titulo) % (10 ** 8))
        if len(id_pelicula) < 8:
            id_pelicula = id_pelicula.zfill(8)
        
        pelicula = [id_pelicula, titulo, director, tupla_genero, puntaje]
        lista_peliculas.append(pelicula)
        
        print(f"\nPelicula cargada con éxito.")
        print(f'ID de Película: {id_pelicula}')
        print(f'Título: {titulo}')
        print(f'Director: {director}')
        print(f'Género: {tupla_genero[1].capitalize()}')
        print(f'Puntaje: {puntaje}/9')
        
        seguir = input(f"\n¿Querés seguir cargando peliculas? (s/n): ")
    lista_a_binario(archivo_peliculas, lista_peliculas)
    return

def baja_de_pelicula():
    lista_peliculas = binario_a_lista(archivo_peliculas)
    print("\n--- Baja de pelicula ---")
    id_baja = input('Ingrese el ID de pelicula: ')
    baja_exitosa = False     
    for pelicula in lista_peliculas:
        if id_baja == pelicula[0]:
            titulo = pelicula[1]
            baja_exitosa = True
            lista_peliculas.remove(pelicula)
    if baja_exitosa:
        lista_a_binario(archivo_peliculas, lista_peliculas)
        pantalla_en_espera(f'\nPelicula "{titulo}" ({id_baja}) dada de baja con éxito.\n')
    else:
        pantalla_en_espera(f'\nLa pelicula {id_baja} no existe en la base de datos.\n')
            
    return lista_peliculas

def listar_pelicula_puntaje():
    lista_peliculas = binario_a_lista(archivo_peliculas)
    max_nombre = max(lista_peliculas, key=lambda i: len(i[1]))[1]
    max_director = max(lista_peliculas, key=lambda i: len(i[2]))[2]
    lista_peliculas.sort(key=lambda x:(-x[4], x[3])) # Ordena por puntaje en forma descendente, y por género en forma ascendente
    print(' Lista de películas por puntaje '.center(40 + max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
    print('ID Pelicula'.ljust(14), 'Nombre'.ljust(max(len(max_nombre) + 2, 8)), 'Director'.ljust(max(len(max_director) + 2, 10)), 'Género'.ljust(15), 'Puntaje\n')
    for pelicula in lista_peliculas:
        id_pelicula, nombre_pelicula, director, genero, puntaje = pelicula
        print(id_pelicula.ljust(14), nombre_pelicula.ljust(max(len(max_nombre) + 2, 8)), director.ljust(max(len(max_director) + 2, 10)), f'{genero[0]} - {genero[1].capitalize()}'.ljust(15), puntaje)
    pantalla_en_espera()
    return

def listar_pelicula_gen():
    '''
    La función lee la lista de peliculas cargada en memoria y hace un corte de
    control por género y por director. Como no usa la función leer_archivo(),
    el corte se hace dentro de un bucle while con una variable usada como
    contador
    '''
    lista_peliculas = binario_a_lista(archivo_peliculas)
    max_nombre = max(lista_peliculas, key=lambda i: len(i[1]))[1]
    max_director = max(lista_peliculas, key=lambda i: len(i[2]))[2]
    lista_peliculas.sort(key=lambda x:(x[3], x[2])) # Ordena por género y por director en forma ascendente
    indice_peliculas = 0
    print(' Lista de películas por género y director '.center(10 + max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
    while indice_peliculas < len(lista_peliculas):
        id_pelicula, nombre_pelicula, director, tupla_genero, puntaje = lista_peliculas[indice_peliculas]
        genero = tupla_genero[1].capitalize()
        genero_anterior = genero
        total_genero = peliculas_genero = 0
        print(f' Género: {genero} '.center(10 + max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
        while genero == genero_anterior:
            director_anterior = director
            total_director = peliculas_director = 0
            print('Director:', (' ' + director).rjust(max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
            print('Nombre'.ljust(max(len(max_nombre) + 2, 8)), 'ID Pelicula'.ljust(14), 'Puntaje')
            while director == director_anterior:
                print(nombre_pelicula.ljust(max(len(max_nombre) + 2, 8)), id_pelicula.ljust(14), puntaje)
                indice_peliculas += 1
                total_director += puntaje
                peliculas_director += 1
                director_anterior = director
                genero_anterior = genero
                try:
                    id_pelicula, nombre_pelicula, director, tupla_genero, puntaje = lista_peliculas[indice_peliculas]
                    genero = tupla_genero[1].capitalize()
                except IndexError:
                    director = genero = ''
            promedio_director = total_director / peliculas_director
            print(f'\nPuntaje promedio: {promedio_director}\n')
            total_genero += total_director
            peliculas_genero += peliculas_director
        promedio_genero = total_genero / peliculas_genero
        print(f'Puntaje promedio ({genero_anterior}): {promedio_genero:.2f}\n')
    pantalla_en_espera()
    return

def asignar_pelicula_usuario():
    '''
    Esta función acepta busqueda de usuarios por ID o por nombre y apellido,
    además usa la librería 'os' para cargar en memoria cada linea del archivo
    de usuarios en forma individual.
    '''
    lista_peliculas = binario_a_lista(archivo_peliculas)
    existe_pelicula = existe_usuario = pelicula_asignada = False
    opcion = '0'
    print("\n--- Asignar película ---")
    titulo = input('Ingrese el nombre de la película: ')
    for pelicula in lista_peliculas:
        if titulo in pelicula:
            id_pelicula = pelicula[0]
            existe_pelicula = True
            while opcion != '1' and opcion != '2':
                print('1. Buscar usuario por nombre y apellido')
                print('2. Buscar usuario por ID')
                opcion = input('\nIngrese una opción: ')
            if opcion == '1':
                usuario = input('Ingrese el nombre y apellido del usuario: ')
                if usuario.islower():
                    usuario = usuario.capitalize()
            elif opcion == '2':
                usuario = str(input('Ingrese el ID del usuario: '))
            with open(f'{ruta}usuarios.csv', 'r') as usuarios_anterior:
                with open(f'{ruta}usuarios_nuevo.csv', 'w') as usuarios_nuevo:
                    id_usuario, nombre, año_nacimiento, peliculas = leer_archivo(usuarios_anterior)
                    while id_usuario != '999zz99':
                        if (opcion == '1' and nombre == usuario) or (opcion == '2' and id_usuario == usuario):
                            existe_usuario = True
                            usuario_encontrado = nombre
                            if peliculas == '':
                                peliculas += str(id_pelicula)
                            elif not id_pelicula in peliculas.split(':'):
                                peliculas += str(':' + id_pelicula)
                            else:
                                pelicula_asignada = True
                        usuarios_nuevo.write(f'{id_usuario},{nombre},{año_nacimiento},{peliculas}\n')
                        id_usuario, nombre, año_nacimiento, peliculas = leer_archivo(usuarios_anterior)
            os.remove(f'{ruta}usuarios.csv')
            os.rename(f'{ruta}usuarios_nuevo.csv', f'{ruta}usuarios.csv')
    if not existe_pelicula:
        pantalla_en_espera(f'\nLa película "{titulo}" no se encuentra en la base de datos.\nPara ver las películas disponibles elija la opción 3 o 4.')
    elif not existe_usuario:
        pantalla_en_espera(f'\nEl usuario "{usuario}" no se encuentra en la base de datos.\nPor favor revise la lista de usuarios registrados.')
    elif pelicula_asignada:
        pantalla_en_espera(f'\nLa película {titulo} ya fue asignada previamente al usuario "{usuario_encontrado}".\nPor favor elija otra película para asignar.')
    else:
        pantalla_en_espera(f'\nPelícula "{titulo}" asignada con éxito al usuario "{usuario_encontrado}".')
    return

def recomendaciones():
    return None

#------- Bloque de inicio -------#
if not os.path.exists(f"{ruta}usuarios_1.csv") and not os.path.exists(archivo_usuarios):
    usuarios = open(archivo_usuarios, "w")
    usuarios.close()
    print('La base de datos de usuarios está vacía. \nDebe dar de alta al menos un usuario antes de elegir otras opciones.')
    pantalla_en_espera()
elif os.path.exists(f"{ruta}usuarios_1.csv") and not os.path.exists(archivo_usuarios):
    print('Se encontró al menos un archivo de usuarios sin cargar en la base de datos. \nDebe realizar un merge para que el programa funcione correctamente.')
    pantalla_en_espera()
menu(mostrar_menu(), ruta)
