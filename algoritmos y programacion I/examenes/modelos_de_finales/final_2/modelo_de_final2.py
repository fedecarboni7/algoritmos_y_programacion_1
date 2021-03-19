"""
Un Bancoregistra los saldos de sus clientes en cada uno de sus productos, para ello cuenta 4
archivos secuenciales en formato CSV uno para cada producto con los saldos de los cliente
ordenado por CUIL, los productos son:
 Caja_ahorros
 Ctas_corrientes
 Acciones
 Fondos de _inversión
Cada uno de estos 4 archivos contiene la siguiente información:
o CUIL
o Sucursal
o Saldo
Se pide confeccionar UN programa PYTHON en forma estructurada y modularizada para
procesar la información de los 4 archivos, de manera de obtener como resultado:
A) Calcular y dejar en un archivo CSV de nombre Saldos, la suma total del saldo de
cada cliente. El archivo tendrá los campos:
a. CUIL
b. y Saldo_acumulado y debe estar ordenado por CUIL.(Un registro por
cliente)
B) Mostrar por pantalla el saldo acumulado de cada sucursal ordenado por
saldo_Sucursal en forma descendente, este saldo surge de la suma de todos los
clientes para cada sucursal)
1. Aclaraciones
 No cargar ningún archivo en memoria
 Leer solo los archivos de entrada y solo una vez cada uno
 Un cliente tiene un solo CUIL
 Un cliente puede tener registros en en 1,2, 3,4 o ningún archivo.
 Pueden venir mas de un registro con CUIL en todos los archivos
"""
MAX_CUIL = '99999999999'

def leer_archivo(archivo):
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip("\n").split(",")
    else:
        registro = [MAX_CUIL, "", ""]
    return registro

def merge_in_dict():

    caja_ahorros = open(r"C:\Users\federico.carboni\Desktop\FIUBA Repo\algoritmos y programacion I\examenes\modelos_de_finales\final_2\caja_ahorros.csv","r")
    ctas_corriente = open(r"C:\Users\federico.carboni\Desktop\FIUBA Repo\algoritmos y programacion I\examenes\modelos_de_finales\final_2\ctas_corriente.csv","r")
    acciones = open(r"C:\Users\federico.carboni\Desktop\FIUBA Repo\algoritmos y programacion I\examenes\modelos_de_finales\final_2\acciones.csv","r")
    fondos_de_inversion = open(r"C:\Users\federico.carboni\Desktop\FIUBA Repo\algoritmos y programacion I\examenes\modelos_de_finales\final_2\fondos_de_inversion.csv","r")

    clave_ca = leer_archivo(caja_ahorros)
    clave_cc = leer_archivo(ctas_corriente)
    clave_a = leer_archivo(acciones)
    clave_fi = leer_archivo(fondos_de_inversion)
    cuil_saldo = {}
    sucursal_saldo = {}

    while clave_ca[0] != MAX_CUIL or clave_cc[0] != MAX_CUIL or clave_a[0] != MAX_CUIL or clave_fi[0] != MAX_CUIL:
        cuil_menor = min(clave_ca[0], clave_cc[0], clave_a[0], clave_fi[0])

        while clave_ca[0] == cuil_menor:
            if clave_ca[0] not in cuil_saldo:
                cuil_saldo[clave_ca[0]] = int(clave_ca[2])
            else:
                cuil_saldo[clave_ca[0]] += int(clave_ca[2])
            if clave_ca[1] not in sucursal_saldo:
                sucursal_saldo[clave_ca[1]] = int(clave_ca[2])
            else:
                sucursal_saldo[clave_ca[1]] += int(clave_ca[2])
            clave_ca = leer_archivo(caja_ahorros)
        
        while clave_cc[0] == cuil_menor:
            if clave_cc[0] not in cuil_saldo:
                cuil_saldo[clave_cc[0]] = int(clave_cc[2])
            else:
                cuil_saldo[clave_cc[0]] += int(clave_cc[2])
            if clave_cc[1] not in sucursal_saldo:
                sucursal_saldo[clave_cc[1]] = int(clave_cc[2])
            else:
                sucursal_saldo[clave_cc[1]] += int(clave_cc[2])
            clave_cc = leer_archivo(ctas_corriente)
        
        while clave_a[0] == cuil_menor:
            if clave_a[0] not in cuil_saldo:
                cuil_saldo[clave_a[0]] = int(clave_a[2])
            else:
                cuil_saldo[clave_a[0]] += int(clave_a[2])
            if clave_a[1] not in sucursal_saldo:
                sucursal_saldo[clave_a[1]] = int(clave_a[2])
            else:
                sucursal_saldo[clave_a[1]] += int(clave_a[2])
            clave_a = leer_archivo(acciones)

        while clave_fi[0] == cuil_menor:
            if clave_fi[0] not in cuil_saldo:
                cuil_saldo[clave_fi[0]] = int(clave_fi[2])
            else:
                cuil_saldo[clave_fi[0]] += int(clave_fi[2])
            if clave_fi[1] not in sucursal_saldo:
                sucursal_saldo[clave_fi[1]] = int(clave_fi[2])
            else:
                sucursal_saldo[clave_fi[1]] += int(clave_fi[2])
            clave_fi = leer_archivo(fondos_de_inversion)
    
    caja_ahorros.close()
    ctas_corriente.close()
    acciones.close()
    fondos_de_inversion.close()

    return cuil_saldo, sucursal_saldo

def dict_process():
    dicc_cuil_saldo, dicc_sucursal_saldo = merge_in_dict()
    # pasamos los datos del dicc cuil-saldo al archivo saldos.csv ordenado por cuil
    archivo_saldos = open(r"C:\Users\federico.carboni\Desktop\FIUBA Repo\algoritmos y programacion I\examenes\modelos_de_finales\final_2\saldos.csv","w")
    for cuil in dicc_cuil_saldo:
        saldo_acumulado = dicc_cuil_saldo[cuil]
        archivo_saldos.write(f"{cuil},{saldo_acumulado}\n")
    archivo_saldos.close()
    # pasamos los datos del dicc sucursal-saldo acumulado a una lista para luego ser imprimido por pantalla ordenado por saldo
    sucursales = list(dicc_sucursal_saldo.items())
    sucursales.sort(key= lambda tupla: tupla[1], reverse= True)
    for sucursal in sucursales:
        print(f"Sucursal: {sucursal[0]} - Saldo acumulado: {sucursal[1]}")

def main():
    dict_process()

main()