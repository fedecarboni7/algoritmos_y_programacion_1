import pickle
import pathlib
import os

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


def pantalla_en_espera(texto=''):
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
    return int(input(f"\nIngrese una opción: "))


def menu(opcion):
    if(opcion == 1):
        submenu_usuarios(mostrar_submenu_usuarios())
    elif(opcion == 2):
        submenu_peliculas(mostrar_submenu_peliculas())
    elif(opcion == 3):
        submenu_recomendaciones(mostrar_submenu_recomendaciones())
    elif(opcion == 4):
        return
    else:
        print(f"\nIngrese una opción del 1 al 4")
    menu(mostrar_menu())
    return


def mostrar_submenu_usuarios():
    print("\n--- Usuarios ---\n")
    print("1. Merge de usuarios")
    print("2. Dar de alta un usuario")
    print("3. Dar de baja un usuario")
    print("4. Listar usuarios por ID")
    print("5. Volver al menú principal")
    return int(input(f"\nIngrese una opción: "))


def submenu_usuarios(opcion):
    if(opcion == 1):
        merge_usuarios()
    elif(opcion == 2):
        alta_de_usuario()
        lista_a_archivo(archivo_usuarios, ordenar(archivo_usuarios))
    elif(opcion == 3):
        baja_de_usuario()
    elif(opcion == 4):
        print('\nGenerando lista...\n')
        listar_por_id(ordenar(archivo_usuarios))
    elif(opcion == 5):
        return
    else:
        print(f"\nIngrese una opción del 1 al 5")
    submenu_usuarios(mostrar_submenu_usuarios())
    return


def merge_usuarios():
    errores = False
    try:
        usuarios_1 = open(f'{ruta}usuarios_1.csv', 'r')
        usuarios_2 = open(f'{ruta}usuarios_2.csv', 'r')
        usuarios_3 = open(f'{ruta}usuarios_3.csv', 'r')
    except FileNotFoundError:
        return print("\nNo hay archivos de usuarios suficientes para generar un merge.\nPor favor elija otra opción.")

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
                id_usuario_error, nombre_error, año_nacimiento_error, peliculas_error = men
                log_error.write(
                    f'{id_usuario_error},{nombre_error},{año_nacimiento_error},{peliculas_error}\n')
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
        print('\nSe encontraron errores en la carga de usuarios, revise "log.txt" para comprobar los usuarios afectados.')
    pantalla_en_espera('\nMerge de usuarios completado con éxito.\n')

    return


def alta_de_usuario():
    if not os.path.exists(archivo_usuarios):
        merge_usuarios()

    with open(archivo_usuarios, 'a') as usuarios:
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
            id_usuario = prefijo_id + nombre[0] + \
                apellido[0] + año_de_nacimiento[2:4]
            usuarios.write(
                f"{id_usuario},{nombre} {apellido},{año_de_nacimiento},\n")

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
        pantalla_en_espera(
            f'\nUsuario "{nombre_usuario}" ({id_baja}) dado de baja con éxito.\n')
    else:
        pantalla_en_espera(
            f'\nEl usuario {id_baja} no existe en la base de datos.\n')
    return


def ordenar(archivo):
    if not os.path.exists(archivo):
        nombre_archivo = archivo.split('\\')[-1]
        print(
            f'ERROR: El archivo {nombre_archivo} no existe, por favor elija otra opción.\n')
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
        print(' Lista de usuarios '.center(
            31 + max(len(nombre_mas_largo) + 2, 22), '-'))
        print('ID Usuario'.ljust(14) + 'Nombre y Apellido'.ljust(
            max(len(nombre_mas_largo) + 2, 22)) + 'Año de Nacimiento\n')
        for usuario in lista_id_ordenados:
            id_usuario, nombre, año_de_nacimiento = usuario[0:3]
            print(id_usuario.ljust(
                14) + nombre.ljust(max(len(nombre_mas_largo) + 2, 22)) + año_de_nacimiento)
        pantalla_en_espera()
    else:
        pantalla_en_espera("No se encuentran usuarios para listar.")
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


def mostrar_submenu_peliculas():
    print("\n--- Peliculas ---\n")
    print("1. Dar de alta una pelicula")
    print("2. Dar de baja una pelicula")
    print("3. Listar las películas por puntaje")
    print("4. Listar las películas ordenadas por género y por director")
    print("5. Asignar una película a un usuario")
    print("6. Volver al menú principal")
    return int(input(f"\nIngrese una opción: "))


def submenu_peliculas(opcion):
    if(opcion == 1):
        alta_de_pelicula()
    elif(opcion == 2):
        baja_de_pelicula()
    elif(opcion == 3):
        print('\nGenerando lista...\n')
        listar_pelicula_puntaje()
    elif(opcion == 4):
        print('\nGenerando lista...\n')
        listar_pelicula_gen()
    elif(opcion == 5):
        asignar_pelicula_usuario()
    elif(opcion == 6):
        return
    else:
        print(f"\nIngrese una opción del 1 al 5")
    submenu_peliculas(mostrar_submenu_peliculas())
    return


def alta_de_pelicula():
    generos = {1: "drama", 2: "comedia", 3: "terror",
               4: "suspenso", 5: "accion", 6: "romantica"}
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
        print("Elija el género:")
        print("1. Drama")
        print("2. Comedia")
        print("3. Terror")
        print("4. Suspenso")
        print("5. Acción")
        print("6. Romantica")
        opcion = int(input("\nIngrese género: "))
        tupla_genero = (opcion, generos[opcion])
        puntaje = int(input("Ingrese puntaje del 1 al 9: "))
        vistas = 0

        id_pelicula = str(hash(titulo) % (10 ** 8))
        if len(id_pelicula) < 8:
            id_pelicula = id_pelicula.zfill(8)

        pelicula = [id_pelicula, titulo, director,
                    tupla_genero, puntaje, vistas]
        lista_peliculas.append(pelicula)

        print(f"\nPelicula cargada con éxito.")
        print(f'ID de Película: {id_pelicula}')
        print(f'Título: {titulo}')
        print(f'Director: {director}')
        print(f'Género: {tupla_genero[1].capitalize()}')
        print(f'Puntaje: {puntaje}/9')

        seguir = input(f"\n¿Querés seguir cargando películas? (s/n): ")
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
        pantalla_en_espera(
            f'\nPelicula "{titulo}" ({id_baja}) dada de baja con éxito.\n')
    else:
        pantalla_en_espera(
            f'\nLa pelicula {id_baja} no existe en la base de datos.\n')

    return lista_peliculas


def listar_pelicula_puntaje():
    lista_peliculas = binario_a_lista(archivo_peliculas)
    max_nombre = max(lista_peliculas, key=lambda i: len(i[1]))[1]
    max_director = max(lista_peliculas, key=lambda i: len(i[2]))[2]
    # Ordena por puntaje en forma descendente, y por género en forma ascendente
    lista_peliculas.sort(key=lambda x: (-x[4], x[3]))
    print(' Lista de películas por puntaje '.center(
        40 + max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
    print('ID Pelicula'.ljust(14), 'Nombre'.ljust(max(len(max_nombre) + 2, 8)),
          'Director'.ljust(max(len(max_director) + 2, 10)), 'Género'.ljust(15), 'Puntaje\n')
    for pelicula in lista_peliculas:
        id_pelicula, nombre_pelicula, director, genero, puntaje, vistas = pelicula
        print(id_pelicula.ljust(14), nombre_pelicula.ljust(max(len(max_nombre) + 2, 8)), director.ljust(
            max(len(max_director) + 2, 10)), f'{genero[0]} - {genero[1].capitalize()}'.ljust(15), puntaje)
    pantalla_en_espera()
    return


def listar_pelicula_gen():
    lista_peliculas = binario_a_lista(archivo_peliculas)
    max_nombre = max(lista_peliculas, key=lambda i: len(i[1]))[1]
    max_director = max(lista_peliculas, key=lambda i: len(i[2]))[2]
    # Ordena por género y por director en forma ascendente
    lista_peliculas.sort(key=lambda x: (x[3], x[2]))
    indice_peliculas = 0
    print(' Lista de películas por género y director '.center(
        10 + max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
    while indice_peliculas < len(lista_peliculas):
        id_pelicula, nombre_pelicula, director, tupla_genero, puntaje, vistas = lista_peliculas[
            indice_peliculas]
        genero = tupla_genero[1].capitalize()
        genero_anterior = genero
        total_genero = peliculas_genero = 0
        print(f' Género: {genero} '.center(
            10 + max(len(max_nombre) + 2, 8) + max(len(max_director) + 2, 10), '-'))
        while genero == genero_anterior:
            director_anterior = director
            total_director = peliculas_director = 0
            print('Director:', (' ' + director).rjust(max(len(max_nombre) +
                                                          2, 8) + max(len(max_director) + 2, 10), '-'))
            print('Nombre'.ljust(max(len(max_nombre) + 2, 8)),
                  'ID Pelicula'.ljust(14), 'Puntaje')
            while director == director_anterior:
                print(nombre_pelicula.ljust(max(len(max_nombre) + 2, 8)),
                      id_pelicula.ljust(14), puntaje)
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
            print(f'\nPuntaje promedio: {promedio_director}\n')
            total_genero += total_director
            peliculas_genero += peliculas_director
        promedio_genero = total_genero / peliculas_genero
        print(f'Puntaje promedio ({genero_anterior}): {promedio_genero:.2f}\n')
    pantalla_en_espera()
    return


def asignar_pelicula_usuario():
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
            with open(archivo_usuarios, 'r') as usuarios_anterior:
                with open(f'{ruta}usuarios_nuevo.csv', 'w') as usuarios_nuevo:
                    id_usuario, nombre, año_nacimiento, peliculas = leer_archivo(
                        usuarios_anterior)
                    while id_usuario != '999zz99':
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
            os.remove(archivo_usuarios)
            os.rename(f'{ruta}usuarios_nuevo.csv', archivo_usuarios)
    lista_a_binario(archivo_peliculas, lista_peliculas)
    if not existe_pelicula:
        pantalla_en_espera(
            f'\nLa película "{titulo}" no se encuentra en la base de datos.\nPara ver las películas disponibles elija la opción 3 o 4.')
    elif not existe_usuario:
        pantalla_en_espera(
            f'\nEl usuario "{usuario}" no se encuentra en la base de datos.\nPor favor revise la lista de usuarios registrados.')
    elif pelicula_asignada:
        pantalla_en_espera(
            f'\nLa película {titulo} ya fue asignada previamente al usuario "{usuario_encontrado}".\nPor favor elija otra película para asignar.')
    else:
        pantalla_en_espera(
            f'\nPelícula "{titulo}" asignada con éxito al usuario "{usuario_encontrado}".')
    return


def mostrar_submenu_recomendaciones():
    print("\n--- Recomendaciones ---\n")
    print("1. Ver las 5 más vistas según género")
    print("2. Recomendar según la última película vista")
    print("3. Volver al menú principal")
    return int(input(f"\nIngrese una opción: "))


def submenu_recomendaciones(opcion):
    if(opcion == 1):
        cinco_mas_vistas()
    elif(opcion == 2):
        recomendacion_ultima_pelicula()
    elif(opcion == 3):
        return
    else:
        print(f"\nIngrese una opción del 1 al 3")
    submenu_recomendaciones(mostrar_submenu_recomendaciones())
    return


def cinco_mas_vistas():
    lista_peliculas = filtrar_por_genero()
    lista_peliculas.sort(key=lambda x: (x[5]), reverse=True)
    for i in range(0, min(len(lista_peliculas), 5)):
        print(lista_peliculas[i])
    return


def filtrar_por_genero():
    generos = {1: "drama", 2: "comedia", 3: "terror",
               4: "suspenso", 5: "accion", 6: "romantica"}
    print("Elija el género:")
    print("1. Drama")
    print("2. Comedia")
    print("3. Terror")
    print("4. Suspenso")
    print("5. Acción")
    print("6. Romántica")
    opcion = int(input("\nIngrese género: "))
    tupla_genero = (opcion, generos[opcion])
    lista_peliculas = binario_a_lista(archivo_peliculas)
    lista_por_genero = []
    for pelicula in lista_peliculas:
        if tupla_genero == pelicula[3]:
            lista_por_genero += [pelicula]
    return lista_por_genero


def buscar_usuario():
    print('1. Buscar usuario por nombre y apellido')
    print('2. Buscar usuario por ID')
    opcion = input('\nIngrese una opción: ')
    if opcion == '1':
        usuario = input('Ingrese el nombre y apellido del usuario: ')
        if usuario.islower():
            usuario = usuario.capitalize()
    elif opcion == '2':
        usuario = str(input('Ingrese el ID del usuario: '))
    with open(archivo_usuarios, 'r') as usuarios:
        id_usuario, nombre, año_nacimiento, peliculas = leer_archivo(usuarios)
        if (opcion == '1' and nombre == usuario) or (opcion == '2' and id_usuario == usuario):
            existe_usuario = True
    if existe_usuario:
        return nombre
    else:
        pantalla_en_espera(
            f'\nEl usuario "{usuario}" no se encuentra en la base de datos.\nPor favor revise la lista de usuarios registrados.')
    return


def peliculas_vistas_usuario():
    nombre = buscar_usuario()
    with open(archivo_usuarios, 'r') as usuarios:
        for usuario in usuarios:
            usuario = usuario.rstrip('\n').split(",")
            if nombre in usuario:
                peliculas_vistas = usuario[3]
                lista_peliculas_vistas = peliculas_vistas.split(":")
    return lista_peliculas_vistas, nombre


def recomendacion_ultima_pelicula():
    peliculas_vistas, nombre = peliculas_vistas_usuario()
    ultima_pelicula_vista = peliculas_vistas[-1]
    dic_peliculas_vistas_otros = {}
    cant_usuarios_misma_pelicula = 0

    with open(archivo_usuarios, 'r') as usuarios:
        for otro_usuario in usuarios:
            otro_usuario = otro_usuario.rstrip('\n').split(",")
            if not (nombre in otro_usuario):
                if ultima_pelicula_vista in otro_usuario[3]:
                    cant_usuarios_misma_pelicula += 1
                    peliculas_vistas_otro = otro_usuario[3].split(':')
                    for pelicula in peliculas_vistas_otro:
                        if not (pelicula == ultima_pelicula_vista):
                            if pelicula in dic_peliculas_vistas_otros:
                                dic_peliculas_vistas_otros[pelicula] += 1
                            else:
                                dic_peliculas_vistas_otros[pelicula] = 1

    for pelicula in peliculas_vistas:
        if pelicula in dic_peliculas_vistas_otros:
            del dic_peliculas_vistas_otros[pelicula]

    lista_peliculas_vistas_otros = sorted(
        dic_peliculas_vistas_otros.items(), key=lambda x: x[1], reverse=True)
    vistas_recomendacion = lista_peliculas_vistas_otros[0][1]
    pelicula_recomendada = lista_peliculas_vistas_otros[0][0]

    lista_peliculas = binario_a_lista(archivo_peliculas)
    for pelicula in lista_peliculas:
        if ultima_pelicula_vista in pelicula:
            ultima_pelicula_vista = pelicula[1]
        elif pelicula_recomendada in pelicula:
            pelicula_recomendada = pelicula[1]

    print(f"De {cant_usuarios_misma_pelicula} usuarios que vieron \"{ultima_pelicula_vista}\", {vistas_recomendacion} también vieron \"{pelicula_recomendada}\".")
    return


def main():
    if not os.path.exists(f"{ruta}usuarios_1.csv") and not os.path.exists(archivo_usuarios):
        usuarios = open(archivo_usuarios, "w")
        usuarios.close()
        print('La base de datos de usuarios está vacía. \nDebe dar de alta al menos un usuario antes de elegir otras opciones.')
        pantalla_en_espera()
    elif os.path.exists(f"{ruta}usuarios_1.csv") and not os.path.exists(archivo_usuarios):
        print('\nSe encontró al menos un archivo de usuarios sin cargar en la base de datos. \nDebe realizar un merge para que el programa funcione correctamente.')
        pantalla_en_espera()
    menu(mostrar_menu())
    return

#------- Bloque de inicio -------#

main()
