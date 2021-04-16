import pickle
import pathlib
import os
from time import sleep

try:
    from colorama import init, Fore, Back, Style
except ModuleNotFoundError:
    import sys
    import subprocess
    print("Módulo 'colorama' no encontrado.\nInstalando módulo...")
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', '<packagename>'])
    from colorama import init, Fore, Back, Style
    init()
else:
    init()

if os.name == 'posix':
    ruta = str(pathlib.Path(__file__).parent.absolute()) + '/archivos/'
else:
    ruta = str(pathlib.Path(__file__).parent.absolute()) + '\\archivos\\'
archivo_usuarios = ruta + 'usuarios.csv'
archivo_peliculas = ruta + 'peliculas.dat'
MAX_ID_USUARIO = '999zz99'


def leer_archivo(archivo):
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        # Condición de salida del while
        registro = [MAX_ID_USUARIO, '', '', '']
    return registro


def limpiar_pantalla():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    return


def pantalla_en_espera():
    if os.name == 'posix':
        input(
            f'\n{Fore.LIGHTBLUE_EX}Presione ENTER para continuar.{Style.RESET_ALL}')
    else:
        input("\nPresione ENTER para continuar.")
    return


def titulo_menu(texto):
    print('\n' + Fore.LIGHTGREEN_EX + Back.BLUE +
          "".center(80, "*") + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + Back.BLUE +
          f'*{texto.center(78, " ")}*' + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + Back.BLUE +
          "".center(80, "*") + Style.RESET_ALL + '\n')
    return


def titulo_submenu(texto):
    print('\n' + Fore.LIGHTCYAN_EX + Back.BLUE +
          "".center(80, "-") + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Back.BLUE +
          f' {texto} '.center(80, "-") + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Back.BLUE +
          "".center(80, "-") + Style.RESET_ALL + '\n')
    return


def titulo_opcion(texto):
    print('\n' + Fore.LIGHTCYAN_EX +
          f' {texto} '.center(80, "-") + Style.RESET_ALL + '\n')
    return


def ingresar_opcion(texto):
    if os.name == 'posix':
        opcion = input(f"\n{Fore.LIGHTBLUE_EX}{texto}{Style.RESET_ALL} ")
    else:
        opcion = input(texto)
    return opcion


def accion_exitosa(texto):
    print(f'{Fore.LIGHTGREEN_EX}{texto}{Style.RESET_ALL}')
    return


def mostrar_error(texto, excepcion=False):
    if '\n' in texto and excepcion:
        lista_texto = texto.split('\n')
        print('\n')
        for cadena in lista_texto:
            print(f"{Fore.LIGHTYELLOW_EX}{Back.RED}{cadena}{Style.RESET_ALL}")
    elif excepcion:
        print(f"{Fore.LIGHTYELLOW_EX}{Back.RED}{texto}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.LIGHTYELLOW_EX}{texto}{Style.RESET_ALL}")
    return


def mostrar_menu():
    titulo_menu('Menú Principal')
    print("1. Usuarios")
    print("2. Películas")
    print("3. Recomendaciones")
    print("4. Salir")
    return ingresar_opcion("\nIngrese una opción: ")


def menu(opcion):
    while opcion != "4":
        while opcion not in ("1", "2", "3", "4"):
            mostrar_error("\nOpción inválida, ingrese una opción del 1 al 4")
            opcion = ingresar_opcion("\nIngrese una opción: ")
        if(opcion == "1"):
            limpiar_pantalla()
            submenu_usuarios(mostrar_submenu_usuarios())
        elif(opcion == "2"):
            limpiar_pantalla()
            submenu_peliculas(mostrar_submenu_peliculas())
        elif(opcion == "3"):
            limpiar_pantalla()
            submenu_recomendaciones(mostrar_submenu_recomendaciones())
        else:
            print(f"\n{Fore.LIGHTBLUE_EX}Cerrando programa...{Style.RESET_ALL}")
            sleep(1)
            return
        limpiar_pantalla()
        opcion = mostrar_menu()



def mostrar_submenu_usuarios():
    titulo_submenu('Usuarios')
    print("1. Merge de usuarios")
    print("2. Dar de alta un usuario")
    print("3. Dar de baja un usuario")
    print("4. Listar usuarios por ID")
    print("5. Volver al menú principal")
    return ingresar_opcion("\nIngrese una opción: ")


def submenu_usuarios(opcion):
    while opcion != "5":
        while opcion not in ("1", "2", "3", "4", "5"):
            mostrar_error("\nOpción inválida, ingrese una opción del 1 al 5")
            opcion = ingresar_opcion("\nIngrese una opción: ")
        if(opcion == "1"):
            limpiar_pantalla()
            merge_usuarios()
        elif(opcion == "2"):
            limpiar_pantalla()
            alta_de_usuario()
            lista_a_archivo(archivo_usuarios, ordenar(archivo_usuarios))
        elif(opcion == "3"):
            limpiar_pantalla()
            baja_de_usuario()
        elif(opcion == "4"):
            print(f'\n{Fore.LIGHTBLUE_EX}Generando lista...{Style.RESET_ALL}\n')
            sleep(1)
            limpiar_pantalla()
            listar_por_id(ordenar(archivo_usuarios))
        else:
            limpiar_pantalla()
            return
        limpiar_pantalla()
        opcion = mostrar_submenu_usuarios()


def merge_usuarios():
    titulo_opcion('Merge de Usuarios')
    errores = False
    try:
        usuarios_1 = open(f'{ruta}usuarios_1.csv', 'r')
        usuarios_2 = open(f'{ruta}usuarios_2.csv', 'r')
        usuarios_3 = open(f'{ruta}usuarios_3.csv', 'r')
    except FileNotFoundError:
        mostrar_error(
            "No hay archivos de usuarios suficientes para generar un merge.\nPor favor elija otra opción.", True)
        pantalla_en_espera()
        return

    print(
        f'\n{Fore.LIGHTBLUE_EX}Generando base de datos de usuarios...{Style.RESET_ALL}')
    sleep(1)
    usuarios = open(archivo_usuarios, 'a')

    id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_archivo(
        usuarios_1)
    clave_usuario_1 = [id_usuario_1, nombre_apellido_1,
                       año_de_nacimiento_1, lista_peliculas_1]

    id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_archivo(
        usuarios_2)
    clave_usuario_2 = [id_usuario_2, nombre_apellido_2,
                       año_de_nacimiento_2, lista_peliculas_2]

    id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_archivo(
        usuarios_3)
    clave_usuario_3 = [id_usuario_3, nombre_apellido_3,
                       año_de_nacimiento_3, lista_peliculas_3]

    clave_anterior = [" ", " ", " ", " "]

    while id_usuario_1 != MAX_ID_USUARIO or id_usuario_2 != MAX_ID_USUARIO or id_usuario_3 != MAX_ID_USUARIO:

        men = min(clave_usuario_1, clave_usuario_2, clave_usuario_3)

        while men[0] == clave_anterior[0]:
            if men[1] != clave_anterior[1] or men[2] != clave_anterior[2]:
                errores = True
                try:
                    log_error = open(f'{ruta}log.txt', 'a')
                except FileNotFoundError:
                    log_error = open(f'{ruta}log.txt', 'w+')

                id_usuario_anterior, nombre_anterior, año_nacimiento_anterior, peliculas_anterior = clave_anterior
                id_usuario_error, nombre_error, año_nacimiento_error, peliculas_error = men

                log_error.write(
                    f'{id_usuario_anterior},{nombre_anterior},{año_nacimiento_anterior} y {id_usuario_error},{nombre_error},{año_nacimiento_error}\n')

                log_error.close()
            else:
                usuarios.write(":{}".format(men[3]))

            clave_anterior = men

            if men == clave_usuario_1:
                clave_usuario_1 = id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_archivo(
                    usuarios_1)
            elif men == clave_usuario_2:
                clave_usuario_2 = id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_archivo(
                    usuarios_2)
            elif men == clave_usuario_3:
                clave_usuario_3 = id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_archivo(
                    usuarios_3)

            men = min(clave_usuario_1, clave_usuario_2, clave_usuario_3)

        if usuarios.tell() != 0:
            usuarios.write("\n")

        clave_anterior = men

        usuarios.write("{},{},{},{}".format(
            clave_anterior[0], clave_anterior[1], clave_anterior[2], clave_anterior[3]))

        if men == clave_usuario_1:
            clave_usuario_1 = id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_archivo(
                usuarios_1)
        elif men == clave_usuario_2:
            clave_usuario_2 = id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_archivo(
                usuarios_2)
        elif men == clave_usuario_3:
            clave_usuario_3 = id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_archivo(
                usuarios_3)

    usuarios.write('\n')

    usuarios_1.close()
    usuarios_2.close()
    usuarios_3.close()
    usuarios.close()

    os.remove(f"{ruta}usuarios_1.csv")
    os.remove(f"{ruta}usuarios_2.csv")
    os.remove(f"{ruta}usuarios_3.csv")

    if errores:
        mostrar_error(
            'Se encontraron errores en la carga de usuarios.\nRevise "log.txt" para comprobar los usuarios afectados.', True)
    accion_exitosa('\nMerge de usuarios completado con éxito.\n')
    pantalla_en_espera()
    limpiar_pantalla()

    return


def alta_de_usuario():
    if not os.path.exists(archivo_usuarios):
        merge_usuarios()
    with open(archivo_usuarios, 'a+') as usuarios:
        seguir = "s"
        while seguir == "s":
            existe_usuario = False
            titulo_opcion("Creación de usuario")
            nombre = ingresar_opcion("Ingrese nombre: ")
            if nombre[0].islower():
                nombre = nombre.capitalize()
            apellido = ingresar_opcion("Ingrese apellido: ")
            if apellido[0].islower():
                apellido = apellido.capitalize()
            nombre_completo = nombre + ' ' + apellido
            año_de_nacimiento = ingresar_opcion("Ingrese año de nacimiento: ")

            usuarios.seek(0)
            linea_archivo_usuarios = leer_archivo(usuarios)
            while not existe_usuario and linea_archivo_usuarios[0] != MAX_ID_USUARIO:
                if nombre_completo == linea_archivo_usuarios[1] and año_de_nacimiento == linea_archivo_usuarios[2]:
                    existe_usuario = True
                linea_archivo_usuarios = leer_archivo(usuarios)

            usuarios.seek(0, 2)
            if existe_usuario:
                mostrar_error(
                    f'\nEl usuario "{nombre_completo}" ya existe en la base de datos.')
            else:
                prefijo_id = str(hash(nombre + apellido) % (10 ** 3))
                if len(prefijo_id) < 3:
                    prefijo_id = prefijo_id.zfill(3)
                id_usuario = prefijo_id + \
                    nombre[0] + apellido[0] + año_de_nacimiento[2:4]
                usuarios.write(
                    f"{id_usuario},{nombre_completo},{año_de_nacimiento},\n")

                accion_exitosa("\nUsuario creado con éxito.")
                accion_exitosa(f'ID de Usuario: {id_usuario}')
                accion_exitosa(f'Nombre y Apellido: {nombre_completo}')
                accion_exitosa(f'Año de nacimiento: {año_de_nacimiento}')

            seguir = ingresar_opcion(
                "\n¿Querés seguir creando usuarios? (s/n): ")
            limpiar_pantalla()
    return


def baja_de_usuario():
    lista_usuarios = ordenar(archivo_usuarios)
    baja_exitosa = False
    titulo_opcion("Baja de usuario")
    id_baja = ingresar_opcion('Ingrese el ID de usuario: ')
    for linea in lista_usuarios:
        if id_baja in linea:
            nombre_usuario = linea[1]
            baja_exitosa = True
            lista_usuarios.remove(linea)

    if baja_exitosa:
        lista_a_archivo(archivo_usuarios, lista_usuarios)
        accion_exitosa(
            f'\nUsuario "{nombre_usuario}" ({id_baja}) dado de baja con éxito.\n')
    else:
        mostrar_error(f'El usuario {id_baja} no existe en la base de datos.\n')
    pantalla_en_espera()
    limpiar_pantalla()
    return


def ordenar(archivo):
    if not os.path.exists(archivo):
        titulo_opcion('Listar usuarios por ID')
        if os.name == 'posix':
            nombre_archivo = archivo.split('/')[-1]
        else:
            nombre_archivo = archivo.split('\\')[-1]
        mostrar_error(
            f'ERROR: El archivo {nombre_archivo} no existe, por favor elija otra opción.', True)
        lista_id_ordenados = []
    else:
        with open(archivo, 'r+') as usuarios_ordenado:
            lista_id_ordenados = []

            id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas = leer_archivo(
                usuarios_ordenado)
            clave_usuario = [id_usuario, nombre_apellido,
                             año_de_nacimiento, lista_peliculas]

            while id_usuario != MAX_ID_USUARIO:
                lista_id_ordenados += [clave_usuario]
                id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas = leer_archivo(
                    usuarios_ordenado)
                clave_usuario = [id_usuario, nombre_apellido,
                                 año_de_nacimiento, lista_peliculas]

        lista_id_ordenados.sort(key=lambda i: i[0])

    return lista_id_ordenados


def listar_por_id(lista_id_ordenados):
    if lista_id_ordenados != []:  # Si la lista está vacía devuelve mensaje de error
        nombre_mas_largo = max(lista_id_ordenados, key=lambda i: len(i[1]))[
            1]  # Devuelve el nombre más largo de la lista
        print(Fore.LIGHTCYAN_EX + ''.center(40 +
                                            max(len(nombre_mas_largo) + 2, 40), '-'))
        print(' Lista de usuarios '.center(
            40 + max(len(nombre_mas_largo) + 2, 40), '-'))
        print(''.center(40 + max(len(nombre_mas_largo) + 2, 40), '-'))
        print('ID Usuario'.ljust(21) + 'Nombre y Apellido'.ljust(
            max(len(nombre_mas_largo) + 2, 42)) + 'Año de Nacimiento\n' + Style.RESET_ALL)
        for usuario in lista_id_ordenados:
            id_usuario, nombre, año_de_nacimiento = usuario[0:3]
            print(id_usuario.ljust(
                21) + nombre.ljust(max(len(nombre_mas_largo) + 2, 42)) + año_de_nacimiento)
        pantalla_en_espera()
    else:
        mostrar_error("No se encuentran usuarios para listar.")
        pantalla_en_espera()
    limpiar_pantalla()
    return


def lista_a_archivo(archivo_usuarios, lista_id_ordenados):
    with open(archivo_usuarios, 'w') as usuarios_ordenado:
        for i in range(len(lista_id_ordenados)):
            usuarios_ordenado.write(
                f"{lista_id_ordenados[i][0]},{lista_id_ordenados[i][1]},{lista_id_ordenados[i][2]},{lista_id_ordenados[i][3]}\n")
    return


def lista_a_binario(archivo, lista):
    with open(archivo, 'wb') as binario:
        pickle.dump(lista, binario)
    return


def binario_a_lista(archivo):
    with open(archivo, 'rb+') as binario:
        lista = pickle.load(binario)
    return lista


def hay_usuarios(archivo_usuarios):
    with open(archivo_usuarios, "r") as usuarios:
        leer_archivo(usuarios)
        bool_hay_usuarios = 0 != usuarios.tell()
    return bool_hay_usuarios


def mostrar_submenu_peliculas():
    titulo_submenu("Peliculas")
    print("1. Dar de alta una pelicula")
    print("2. Dar de baja una pelicula")
    print("3. Listar las películas por puntaje")
    print("4. Listar las películas ordenadas por género y por director")
    print("5. Asignar una película a un usuario")
    print("6. Volver al menú principal")
    return ingresar_opcion("\nIngrese una opción: ")


def submenu_peliculas(opcion):
    while opcion != "6":
        while opcion not in ("1", "2", "3", "4", "5", "6"):
            mostrar_error("\nOpción inválida, ingrese una opción del 1 al 6")
            opcion = ingresar_opcion("\nIngrese una opción: ")
        if(opcion == "1"):
            limpiar_pantalla()
            alta_de_pelicula()
        elif(opcion == "2"):
            limpiar_pantalla()
            baja_de_pelicula()
        elif(opcion == "3"):
            print(f'\n{Fore.LIGHTBLUE_EX}Generando lista...{Style.RESET_ALL}\n')
            sleep(1)
            limpiar_pantalla()
            listar_pelicula_puntaje()
        elif(opcion == "4"):
            print(f'\n{Fore.LIGHTBLUE_EX}Generando lista...{Style.RESET_ALL}\n')
            sleep(1)
            limpiar_pantalla()
            listar_pelicula_gen()
        elif(opcion == "5"):
            limpiar_pantalla()
            asignar_pelicula_usuario()
        else:
            limpiar_pantalla()
            return
        limpiar_pantalla()
        opcion = mostrar_submenu_peliculas()


def alta_de_pelicula():
    generos = {1: "drama", 2: "comedia", 3: "terror",
               4: "suspenso", 5: "accion", 6: "romantica"}
    seguir = "s"
    lista_peliculas = binario_a_lista(archivo_peliculas)
    while seguir == "s":
        existe_pelicula = False
        titulo_opcion("Alta de película")
        titulo = ingresar_opcion("Ingrese título: ")
        if titulo[0].islower():
            titulo = titulo.capitalize()
        director_nombre = ingresar_opcion("Ingrese nombre del director: ")
        if director_nombre[0].islower():
            director_nombre = director_nombre.capitalize()
        director_apellido = ingresar_opcion("Ingrese apellido del director: ")
        if director_apellido[0].islower():
            director_apellido = director_apellido.capitalize()
        director = director_apellido + ', ' + director_nombre

        for p in lista_peliculas:
            if titulo == p[1] and director == p[2]:
                existe_pelicula = True
                break

        if existe_pelicula:
            mostrar_error(
                f'La película "{titulo}" de {director_nombre} {director_apellido} ya existe en la base de datos.')
        else:
            print("\nElija el genero:")
            print("1. Drama")
            print("2. Comedia")
            print("3. Terror")
            print("4. Suspenso")
            print("5. Acción")
            print("6. Romantica")
            opcion = int(ingresar_opcion("\nIngrese genero: "))
            tupla_genero = (opcion, generos[opcion])
            puntaje = int(ingresar_opcion("Ingrese puntaje del 1 al 9: "))
            vistas = 0

            id_pelicula = str(hash(titulo) % (10 ** 8))
            if len(id_pelicula) < 8:
                id_pelicula = id_pelicula.zfill(8)

            pelicula = [id_pelicula, titulo, director,
                        tupla_genero, puntaje, vistas]
            lista_peliculas.append(pelicula)

            accion_exitosa("\nPelicula cargada con éxito.")
            accion_exitosa(f'ID de Película: {id_pelicula}')
            accion_exitosa(f'Título: {titulo}')
            accion_exitosa(f'Director: {director}')
            accion_exitosa(f'Género: {tupla_genero[1].capitalize()}')
            accion_exitosa(f'Puntaje: {puntaje}/9')

        seguir = ingresar_opcion(
            "\n¿Querés seguir cargando peliculas? (s/n): ")
        limpiar_pantalla()
    lista_a_binario(archivo_peliculas, lista_peliculas)
    return


def baja_de_pelicula():
    lista_peliculas = binario_a_lista(archivo_peliculas)
    titulo_opcion("Baja de pelicula")
    id_baja = ingresar_opcion('Ingrese el ID de pelicula: ')
    baja_exitosa = False
    for pelicula in lista_peliculas:
        if id_baja == pelicula[0]:
            titulo = pelicula[1]
            baja_exitosa = True
            lista_peliculas.remove(pelicula)
    if baja_exitosa:
        lista_a_binario(archivo_peliculas, lista_peliculas)
        accion_exitosa(
            f'\nPelicula "{titulo}" ({id_baja}) dada de baja con éxito.\n')
    else:
        mostrar_error(
            f'La pelicula {id_baja} no existe en la base de datos.\n')
    pantalla_en_espera()
    limpiar_pantalla()
    return


def listar_pelicula_puntaje():
    lista_peliculas = binario_a_lista(archivo_peliculas)
    max_nombre = max(lista_peliculas, key=lambda i: len(i[1]))[1]
    max_director = max(lista_peliculas, key=lambda i: len(i[2]))[2]
    # Ordena por puntaje en forma descendente, y por género en forma ascendente
    lista_peliculas.sort(key=lambda x: (-x[4], x[3]))
    print(Fore.LIGHTCYAN_EX + ''.center(37 +
                                        max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
    print(' Lista de películas por puntaje '.center(
        37 + max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
    print(''.center(37 + max(len(max_nombre) + 2, 8) +
                    max(len(max_director) + 2, 10), '-'))
    print('ID Pelicula'.ljust(15) + 'Nombre'.ljust(max(len(max_nombre) + 3, 8)) + 'Director'.ljust(
        max(len(max_director) + 3, 10)) + 'Género'.ljust(13) + 'Puntaje' + Style.RESET_ALL + '\n')
    for pelicula in lista_peliculas:
        id_pelicula, nombre_pelicula, director, genero, puntaje, vistas = pelicula
        print(id_pelicula.ljust(14), nombre_pelicula.ljust(max(len(max_nombre) + 2, 8)), director.ljust(
            max(len(max_director) + 2, 10)), f'{genero[0]} - {genero[1].capitalize()}'.ljust(13), f'{puntaje}/9')
    pantalla_en_espera()
    limpiar_pantalla()
    return


def listar_pelicula_gen():
    lista_peliculas = binario_a_lista(archivo_peliculas)
    max_nombre = max(lista_peliculas, key=lambda i: len(i[1]))[1]
    max_director = max(lista_peliculas, key=lambda i: len(i[2]))[2]
    # Ordena por género y por director en forma ascendente
    lista_peliculas.sort(key=lambda x: (x[3], x[2]))
    indice_peliculas = 0
    while indice_peliculas < len(lista_peliculas):
        print(Fore.LIGHTCYAN_EX + ''.center(37 + max(len(max_nombre) +
                                                     2, 8) + max(len(max_director) + 2, 10), '-'))
        print(' Lista de películas por género y director '.center(
            37 + max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
        print(''.center(37 + max(len(max_nombre) + 2, 8) +
                        max(len(max_director) + 2, 10), '-') + Style.RESET_ALL)
        id_pelicula, nombre_pelicula, director, tupla_genero, puntaje, vistas = lista_peliculas[
            indice_peliculas]
        genero = tupla_genero[1].capitalize()
        genero_anterior = genero
        total_genero = peliculas_genero = 0
        print(Fore.LIGHTBLUE_EX + f' Género: {genero} '.center(37 + max(
            len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-') + Style.RESET_ALL)
        while genero == genero_anterior:
            director_anterior = director
            total_director = peliculas_director = 0
            print(Fore.LIGHTBLUE_EX + 'Director:', (' ' + director).rjust(27 +
                                                                          max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-') + Style.RESET_ALL)
            print('Nombre'.ljust(max(len(max_nombre) + 2, 28)),
                  'ID Pelicula'.ljust(34), 'Puntaje')
            while director == director_anterior:
                print(nombre_pelicula.ljust(max(len(max_nombre) + 2, 28)),
                      id_pelicula.ljust(34), f'{puntaje}/9')
                indice_peliculas += 1
                total_director += puntaje
                peliculas_director += 1
                director_anterior = director
                genero_anterior = genero
                try:
                    id_pelicula, nombre_pelicula, director, tupla_genero, puntaje, vistas = lista_peliculas[
                        indice_peliculas]
                    genero = tupla_genero[1].capitalize()
                except IndexError:
                    director = genero = ''
            promedio_director = total_director / peliculas_director
            print(Fore.LIGHTBLUE_EX +
                  f'\nPuntaje promedio: {promedio_director}\n' + Style.RESET_ALL)
            total_genero += total_director
            peliculas_genero += peliculas_director
        promedio_genero = total_genero / peliculas_genero
        print(Fore.LIGHTGREEN_EX +
              f'Puntaje promedio ({genero_anterior}): {promedio_genero:.2f}\n' + Style.RESET_ALL)
        pantalla_en_espera()
        limpiar_pantalla()
    return


def asignar_pelicula_usuario():
    lista_peliculas = binario_a_lista(archivo_peliculas)
    existe_pelicula = existe_usuario = pelicula_asignada = False
    opcion = '0'
    titulo_opcion("Asignar película")
    titulo = ingresar_opcion('Ingrese el nombre de la película: ')
    for pelicula in lista_peliculas:
        if titulo in pelicula:
            id_pelicula = pelicula[0]
            existe_pelicula = True
            while opcion != '1' and opcion != '2':
                print('1. Buscar usuario por nombre y apellido')
                print('2. Buscar usuario por ID')
                opcion = ingresar_opcion('\nIngrese una opción: ')
            if opcion == '1':
                usuario = ingresar_opcion(
                    'Ingrese el nombre y apellido del usuario: ')
                if usuario.islower():
                    usuario = usuario.capitalize()
            elif opcion == '2':
                usuario = str(ingresar_opcion('Ingrese el ID del usuario: '))
            with open(archivo_usuarios, 'r') as usuarios_anterior:
                with open(f'{ruta}usuarios_nuevo.csv', 'w') as usuarios_nuevo:
                    id_usuario, nombre, año_nacimiento, peliculas = leer_archivo(
                        usuarios_anterior)
                    while id_usuario != MAX_ID_USUARIO:
                        if (opcion == '1' and nombre == usuario) or (opcion == '2' and id_usuario == usuario):
                            existe_usuario = True
                            usuario_encontrado = nombre
                            if peliculas == '':
                                peliculas += str(id_pelicula)
                                pelicula[5] += 1
                            elif not id_pelicula in peliculas.split(':'):
                                peliculas += str(':' + id_pelicula)
                                pelicula[5] += 1
                            else:
                                pelicula_asignada = True
                        usuarios_nuevo.write(
                            f'{id_usuario},{nombre},{año_nacimiento},{peliculas}\n')
                        id_usuario, nombre, año_nacimiento, peliculas = leer_archivo(
                            usuarios_anterior)
            os.remove(f'{ruta}usuarios.csv')
            os.rename(f'{ruta}usuarios_nuevo.csv', archivo_usuarios)
    lista_a_binario(archivo_peliculas, lista_peliculas)
    if not existe_pelicula:
        mostrar_error(
            f'La película "{titulo}" no se encuentra en la base de datos.\nPara ver las películas disponibles elija la opción 3 o 4.')
    elif not existe_usuario:
        mostrar_error(
            f'El usuario "{usuario}" no se encuentra en la base de datos.\nPor favor revise la lista de usuarios registrados.')
    elif pelicula_asignada:
        mostrar_error(
            f'La película {titulo} ya fue asignada previamente al usuario "{usuario_encontrado}".\nPor favor elija otra película para asignar.')
    else:
        accion_exitosa(
            f'\nPelícula "{titulo}" asignada con éxito al usuario "{usuario_encontrado}".')
    pantalla_en_espera()
    limpiar_pantalla()
    return


def mostrar_submenu_recomendaciones():
    titulo_submenu("Recomendaciones")
    print("1. Ver las 5 más vistas según género")
    print("2. Recomendar según la última película vista")
    print("3. Volver al menú principal")
    return ingresar_opcion("\nIngrese una opción: ")


def submenu_recomendaciones(opcion):
    while opcion != "3":
        while opcion not in ("1", "2", "3"):
            mostrar_error("\nOpción inválida, ingrese una opción del 1 al 3")
            opcion = ingresar_opcion("\nIngrese una opción: ")
        if(opcion == "1"):
            limpiar_pantalla()
            cinco_mas_vistas()
        elif(opcion == "2"):
            limpiar_pantalla()
            recomendacion_ultima_pelicula()
        else:
            limpiar_pantalla()
            return
        limpiar_pantalla()
        opcion = mostrar_submenu_recomendaciones()


def cinco_mas_vistas():
    titulo_opcion('5 películas más vistas, por género')
    genero, lista_peliculas = filtrar_por_genero()
    if lista_peliculas == []:
        mostrar_error(
            f'No hay películas de género {genero} en la base de datos.')
    else:
        max_nombre = max(lista_peliculas, key=lambda i: len(i[1]))[1]
        max_director = max(lista_peliculas, key=lambda i: len(i[2]))[2]
        lista_peliculas.sort(key=lambda x: (x[5]), reverse=True)
        print('\n' + Fore.LIGHTCYAN_EX + ''.center(40 +
                                                   max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
        print(f' Películas de {genero} más vistas '.center(
            40 + max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
        print(''.center(40 + max(len(max_nombre) + 2, 8) +
                        max(len(max_director) + 2, 10), '-'))
        print('ID Pelicula'.ljust(14), 'Nombre'.ljust(max(len(max_nombre) + 2, 21)), 'Director'.ljust(
            max(len(max_director) + 2, 21)), 'Puntaje'.ljust(10), f'Vistas{Style.RESET_ALL}\n')
        for i in range(0, min(len(lista_peliculas), 5)):
            id_pelicula, nombre_pelicula, director, genero, puntaje, vistas = lista_peliculas[
                i]
            print(id_pelicula.ljust(14), nombre_pelicula.ljust(max(len(max_nombre) + 2, 21)),
                  director.ljust(max(len(max_director) + 2, 21)), f'{puntaje}/9'.ljust(10), vistas)
    pantalla_en_espera()
    limpiar_pantalla()
    return


def filtrar_por_genero():
    generos = {1: "drama", 2: "comedia", 3: "terror",
               4: "suspenso", 5: "accion", 6: "romantica"}
    print("\nElija el genero:")
    print("1. Drama")
    print("2. Comedia")
    print("3. Terror")
    print("4. Suspenso")
    print("5. Acción")
    print("6. Romantica")
    opcion = int(ingresar_opcion("\nIngrese genero: "))
    tupla_genero = (opcion, generos[opcion])
    lista_peliculas = binario_a_lista(archivo_peliculas)
    lista_por_genero = []
    for pelicula in lista_peliculas:
        if tupla_genero == pelicula[3]:
            lista_por_genero += [pelicula]
    return generos[opcion], lista_por_genero


def buscar_usuario():
    '''
    Busca un nombre o ID de usuario en la base de datos.
    Devuelve una lista vacía si el usuario no existe
    '''
    id_usuario = ""
    existe_usuario = False
    opcion = '0'
    while opcion != '1' and opcion != '2':
        print('1. Buscar usuario por nombre y apellido')
        print('2. Buscar usuario por ID')
        opcion = ingresar_opcion('\nIngrese una opción: ')
    if opcion == '1':
        usuario = ingresar_opcion(
            '\nIngrese el nombre y apellido del usuario: ')
        if ' ' in usuario:
            nombre_completo = usuario.split(' ')
            nombre_usuario, apellido_usuario = nombre_completo
            if nombre_usuario.islower():
                nombre_usuario = nombre_usuario.capitalize()
            if apellido_usuario.islower():
                apellido_usuario = apellido_usuario.capitalize()
            usuario = nombre_usuario + ' ' + apellido_usuario
    elif opcion == '2':
        usuario = str(ingresar_opcion('\nIngrese el ID del usuario: '))
    with open(archivo_usuarios, 'r') as usuarios:
        while not existe_usuario and id_usuario != MAX_ID_USUARIO:
            id_usuario, nombre, año_nacimiento, peliculas = leer_archivo(
                usuarios)
            if (opcion == '1' and nombre == usuario) or (opcion == '2' and id_usuario == usuario):
                existe_usuario = True
    if not existe_usuario:
        mostrar_error(
            f'El usuario "{usuario}" no se encuentra en la base de datos.\nPor favor revise la lista de usuarios registrados.')
        usuario = []
        pantalla_en_espera()
        limpiar_pantalla()
    else:
        usuario = [id_usuario, nombre, año_nacimiento, peliculas]
    return usuario


def peliculas_vistas_usuario():
    '''
    Genera una lista con los ID de películas vistas por el usuario.
    Devuelve None como nombre y lista vacía si no existe el usuario.
    '''
    lista_peliculas_vistas = []
    usuario = buscar_usuario()

    if usuario != []:
        id_usuario, nombre, año_nacimiento, peliculas = usuario
        lista_peliculas_vistas = peliculas.split(":")
    else:
        nombre = None
    return lista_peliculas_vistas, nombre


def recomendacion_ultima_pelicula():
    '''
    Si el nombre de usuario es distinto a None, genera una lista de películas
    vistas por quienes vieron la última película del usuario, y recomienda la
    película más vista.
    '''
    titulo_opcion('Recomendar según la última película vista')
    peliculas_vistas, nombre = peliculas_vistas_usuario()
    if nombre != None:
        ultima_pelicula_vista = peliculas_vistas[-1]
        dic_peliculas_vistas_otros = {}
        cant_usuarios_misma_pelicula = 0
        # Buscar otras películas vistas por usuarios que hayan visto la última película
        with open(archivo_usuarios, 'r') as usuarios:
            id_otro_usuario, nombre_otro_usuario, año_nacimiento_otro_usuario, peliculas_otro_usuario = leer_archivo(
                usuarios)
            while id_otro_usuario != MAX_ID_USUARIO:
                if nombre != nombre_otro_usuario:
                    if ultima_pelicula_vista in peliculas_otro_usuario:
                        cant_usuarios_misma_pelicula += 1
                        peliculas_vistas_otro = peliculas_otro_usuario.split(
                            ':')
                        for pelicula in peliculas_vistas_otro:
                            if pelicula != ultima_pelicula_vista:
                                if pelicula in dic_peliculas_vistas_otros:
                                    dic_peliculas_vistas_otros[pelicula] += 1
                                else:
                                    dic_peliculas_vistas_otros[pelicula] = 1
                id_otro_usuario, nombre_otro_usuario, año_nacimiento_otro_usuario, peliculas_otro_usuario = leer_archivo(
                    usuarios)
        # Quitar la última película del usuario de la lista de películas a recomendar
        for pelicula in peliculas_vistas:
            if pelicula in dic_peliculas_vistas_otros:
                del dic_peliculas_vistas_otros[pelicula]
        # Ordenar las películas y elegir la más vista
        if dic_peliculas_vistas_otros != {}:
            lista_peliculas_vistas_otros = sorted(
                dic_peliculas_vistas_otros.items(), key=lambda x: x[1], reverse=True)
            vistas_recomendacion = lista_peliculas_vistas_otros[0][1]
            pelicula_recomendada = lista_peliculas_vistas_otros[0][0]
            # Buscar los nombres de las películas a partir del ID
            lista_peliculas = binario_a_lista(archivo_peliculas)
            for pelicula in lista_peliculas:
                if ultima_pelicula_vista in pelicula:
                    ultima_pelicula_vista = pelicula[1]
                elif pelicula_recomendada in pelicula:
                    pelicula_recomendada = pelicula[1]
            # Imprimir resultado
            accion_exitosa(
                f'\nÚltima pelicula vista por {nombre}: {ultima_pelicula_vista}')
            accion_exitosa(
                f'De {cant_usuarios_misma_pelicula} usuarios que vieron "{ultima_pelicula_vista}", {vistas_recomendacion} también vieron "{pelicula_recomendada}".')
        else:
            mostrar_error(
                '\nNo hay suficientes datos para hacer una recomendación.')
        pantalla_en_espera()
    return


def main():
    limpiar_pantalla()
    titulo_menu('BIENVENIDO A NETFLIP')
    sleep(2)
    if not os.path.exists(f"{ruta}usuarios_1.csv") and not os.path.exists(archivo_usuarios):
        usuarios = open(archivo_usuarios, "w")
        usuarios.close()
        mostrar_error(
            'La base de datos de usuarios está vacía.\nDebe dar de alta al menos un usuario antes de elegir otras opciones.', True)
        pantalla_en_espera()
    elif os.path.exists(f"{ruta}usuarios_1.csv") and not os.path.exists(archivo_usuarios):
        mostrar_error(
            'Se encontró al menos un archivo de usuarios sin cargar en la base de datos.\nDebe realizar un merge para que el programa funcione correctamente.', True)
        pantalla_en_espera()
    limpiar_pantalla()
    menu(mostrar_menu())
    return

#------- Bloque de inicio -------#


main()
