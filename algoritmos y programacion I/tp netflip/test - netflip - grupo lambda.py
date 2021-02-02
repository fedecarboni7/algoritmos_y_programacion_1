import pickle

ruta = "C:\\Users\\federico.carboni\\Desktop\\FIUBA Repo\\algoritmos y programacion I\\tp netflip\\archivos\\"
#ruta = "C:\\Users\\feden\\Documents\\Programación\\repositorios git\\fiuba\\algoritmos y programacion I\\tp netflip\\archivos\\"

def leer_info(archivo):
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        registro = ['zzzz9999','','',''] # Condición de salida del while
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
        usuarios(mostrar_submenu_usuarios(), ruta)
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

def mostrar_submenu_usuarios():
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
        usuarios(mostrar_submenu_usuarios(), ruta)
    elif(opcion == 2):
        alta_de_usuario(ruta)
        usuarios(mostrar_submenu_usuarios(), ruta)
    elif(opcion == 3):
        baja_de_usuario()
        usuarios(mostrar_submenu_usuarios(), ruta)
    elif(opcion == 4):
        merge_usuarios(ruta)
        listar_por_id(ordenar(ruta, "usuarios_merge.csv"))
        usuarios(mostrar_submenu_usuarios(), ruta)
    elif(opcion != 5):
        print(f"\nIngrese una opción del 1 al 5")
        usuarios(mostrar_submenu_usuarios(), ruta)
    return

def merge_usuarios(ruta):
    try:
        lista_a_archivo(ruta, "usuarios_1.csv", ordenar(ruta, "usuarios_1.csv"))
        usuarios_1 = open(f'{ruta}usuarios_1.csv','r')
    except FileNotFoundError:
        usuarios_1 = open(f'{ruta}usuarios_1.csv','w+')
    try:
        lista_a_archivo(ruta, "usuarios_2.csv", ordenar(ruta, "usuarios_2.csv"))
        usuarios_2 = open(f'{ruta}usuarios_2.csv','r')
    except FileNotFoundError:
        usuarios_2 = open(f'{ruta}usuarios_2.csv','w+')
    try:
        lista_a_archivo(ruta, "usuarios_2.csv", ordenar(ruta, "usuarios_2.csv"))
        usuarios_3 = open(f'{ruta}usuarios_3.csv','r')
    except FileNotFoundError:
        usuarios_3 = open(f'{ruta}usuarios_3.csv','w+')
    
    usuarios_merge = open(f'{ruta}usuarios_merge.csv','w')
    
    if not hay_usuarios(usuarios_1) and not hay_usuarios(usuarios_2) and not hay_usuarios(usuarios_3):
        return print("\nNo se encuentran usuarios creados, por favor cree uno")

    id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1 = leer_info(usuarios_1)
    clave_usuario_1 =[id_usuario_1, nombre_apellido_1, año_de_nacimiento_1, lista_peliculas_1]
    
    id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2 = leer_info(usuarios_2)
    clave_usuario_2 = [id_usuario_2, nombre_apellido_2, año_de_nacimiento_2, lista_peliculas_2]

    id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3 = leer_info(usuarios_3)
    clave_usuario_3 = [id_usuario_3, nombre_apellido_3, año_de_nacimiento_3, lista_peliculas_3]

    max = "zzzz9999"
    clave_anterior = [" "," "," "," "]

    while id_usuario_1 != max or id_usuario_2 != max or id_usuario_3 != max :

        men = min(clave_usuario_1, clave_usuario_2, clave_usuario_3)
        
        while men[0] == clave_anterior[0]:
            if men[1] != clave_anterior[1] or men[2] != clave_anterior[2]:
                try:
                    log_error = open(f'{ruta}log.txt','a')
                except FileNotFoundError:
                    log_error = open(f'{ruta}log.txt','w+')
                log_error.write(f"Los datos personales en {men[0:3]} y {clave_anterior[0:3]} no coinciden\n")
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

    usuarios_1.close()
    usuarios_2.close()
    usuarios_3.close()
    usuarios_merge.close()

    return

def hay_usuarios(archivo_usuarios):
    leer_info(archivo_usuarios)
    hay_usuarios = 0 != archivo_usuarios.tell()
    archivo_usuarios.seek(0)
    return hay_usuarios

def alta_de_usuario(ruta):
    with open(f'{ruta}usuarios_1.csv','a') as usuarios_1:
        seguir = "s"
        while seguir == "s":
            print("\n--- Creación de usuario ---")
            nombre = input(f"Ingrese nombre: ")
            apellido = input(f"Ingrese apellido: ")
            año_de_nacimiento = input(f"Ingrese año de nacimiento: ")
            if len(apellido) > 3:
                id_usuario = nombre[0] + apellido[0:3] + año_de_nacimiento
            else:
                id_usuario = nombre[0] + apellido + año_de_nacimiento
            print(f"\nUsuario creado con éxito. Tu ID es: {id_usuario}")
            
            usuarios_1.write(f"{id_usuario}, {nombre} {apellido}, {año_de_nacimiento},\n")

            seguir = input(f"\n¿Querés seguir creando usuarios? (s/n): ")

    return

def baja_de_usuario():
    return None

def ordenar(ruta, archivo):
    with open(f'{ruta}{archivo}','r+') as usuarios_ordenado:
        max = "zzzz9999"
        lista_id_ordenados = []

        id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas = leer_info(usuarios_ordenado)
        clave_usuario = [id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas]
        
        while id_usuario != max:
            lista_id_ordenados += [clave_usuario]
            id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas = leer_info(usuarios_ordenado)
            clave_usuario = [id_usuario, nombre_apellido, año_de_nacimiento, lista_peliculas]
    
    lista_id_ordenados.sort(key=lambda i: i[0])

    return lista_id_ordenados

def lista_a_archivo(ruta, archivo, lista_id_ordenados):
    with open(f'{ruta}{archivo}','w') as usuarios_ordenado:
        
        for i in range(len(lista_id_ordenados)):
            usuarios_ordenado.write(f"{lista_id_ordenados[i][0]},{lista_id_ordenados[i][1]},{lista_id_ordenados[i][2]},{lista_id_ordenados[i][3]}\n")

    return

def listar_por_id(lista_id_ordenados):
    for usuario in lista_id_ordenados:
        print(usuario)
    return

def peliculas():
    return None

def recomendaciones():
    return None

#------- Bloque de inicio -------#
menu(mostrar_menu(), ruta)