# Ejercicio clase archivos de texto (csv).
# Recorrer el archivo maestro de clientes, y aplicar al saldo del cliente una
# actualización del 50%. Mostrar los datos del cliente, con su saldo original y
# el actualizado. Al mismo tiempo, generar un nuevo archivo que contenga en lugar
# del saldo original, el saldo actualizado.

def leer_archivo(archivo):
    linea = archivo.readline()
    if linea:
        linea = linea.strip("\n")
    else:
        linea = ",,"
    return linea.split(",")


def mostrar_datos(nro, nom_ape, saldo_original, saldo_actualizado):
    print("Cliente: {0} - {1}".format(nro, nom_ape))
    print("Saldo original: {0:5d} - Saldo actualizado: {1:5d}\n".format(
        saldo_original, saldo_actualizado))
    return


def salvar_datos(archivo, nro, nom_ape, saldo):
    linea = "{},{},{}\n".format(nro, nom_ape, saldo)
    archivo.write(linea)
    return


def procesar_archivo(fmaestro, fmaestro_nuevo):
    nro, nom_ape, saldo = leer_archivo(fmaestro)
    while nro:
        saldo = int(saldo)
        saldo_actualizado = int(saldo * 1.5)
        mostrar_datos(nro, nom_ape, saldo, saldo_actualizado)
        salvar_datos(fmaestro_nuevo, nro, nom_ape, saldo_actualizado)
        nro, nom_ape, saldo = leer_archivo(fmaestro)
    return

################### Bloque Principal ###################


fmaestro = open(
    "C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\maestro.csv")
fmaestro_nuevo = open(
    "C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\maenuevo.csv", "w")
procesar_archivo(fmaestro, fmaestro_nuevo)
fmaestro.close()
fmaestro_nuevo.close()
