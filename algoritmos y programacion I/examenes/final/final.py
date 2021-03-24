"""La veterinaria “Gatuna” se especializa en atención de gatos. Este nuevo año están en plena
campaña de vacunación y para eso están almacenando la información en un archivo
VACUNACION.CSV (que NO entra en memoria) de la siguiente forma:
Nombre del gato (string), DNI del dueño (string de 8 caracteres), fecha (string en formato
AAAAMMDD), costo (float).
Se cuenta además con un archivo vencimientos.py que tiene cargada la información del año
pasado como un diccionario de esta forma:
vtos = {
 “30083856” : {“Gunilla”: “20210217”},
 “12857290” : {“Michina”: “20210131”, “Tom”: “20210115”},
}
La clave es el DNI del dueño y su valor es un diccionario con el nombre del gato como clave y
la fecha de vencimiento como valor.
Se pide:
1) Procesar el archivo de vacunaciones y generar un nuevo diccionarios vtos_2022 con
un formato equivalente al diccionario vtos. El vencimiento de todas las vacunas es al
año exacto de la fecha de vacunación. Imprimirlo por pantalla.
2) En caso de detectar que algún gato haya sido vacunado en una fecha posterior al
vencimiento de su vacuna, grabar un mensaje relevante en una nueva línea en un
archivo ADVERTENCIAS.TXT. En ese mismo archivo generar otro mensaje para todos
los gatos que no hayan sido re-vacunados este año todavía.
3) Generar un top 15 de clientes según el gasto total en vacunas para generarles un
voucher de descuento, imprimir el listado ordenado por pantalla. """

from vencimientos import vtos

MAX_DNI = "999999999"
vtos_2022 = {}
top_clientes = {}

def leer_archivo(archivo):
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip("\n").split(",")
    else:
        registro = ["", MAX_DNI, "", float(0)]
    return registro

def generar_vtos_2022():
    vacunaciones = open(r"C:\Users\feden\Documents\Programación\repositorios git\fiuba\algoritmos y programacion I\examenes\final\vacunacion.csv", "r")
    advertencias = open(r"C:\Users\feden\Documents\Programación\repositorios git\fiuba\algoritmos y programacion I\examenes\final\advertencias.txt", "w")
    gato, dni, fecha, costo = leer_archivo(vacunaciones)

    while dni != MAX_DNI:
        año = int(fecha[0:4])

        nuevo_vto = f"{año + 1}{fecha[4:]}"
        if dni not in vtos_2022:
            vtos_2022[dni] = {gato: nuevo_vto}
        else:
            vtos_2022[dni][gato] = nuevo_vto
        
        if vtos[dni][gato] < fecha:
            advertencias.write(f"El gato: {gato} del cliente con DNI: {dni} fue vacunado despues de la fecha de vencimiento de su ultima vacuna\n")

        if año < 2021:
            advertencias.write(f"El gato: {gato} del cliente con DNI: {dni} no fue vacunado en el 2021 todavia\n")

        if dni not in top_clientes:
            top_clientes[dni] = float(costo)
        else:
            top_clientes[dni] += float(costo)
    
        gato, dni, fecha, costo = leer_archivo(vacunaciones)
    
    vacunaciones.close()

def imprimir_vtos2022():
    for dni in vtos_2022:
        print(f"“{dni}”: {vtos_2022[dni]}")

def imprimir_top_clientes():
    contador = 1
    lista_top_clientes = list(top_clientes.items())
    lista_top_clientes.sort(key= lambda cliente: cliente[1], reverse=True)
    lista_top_clientes[0:16]
    print(f"\nTop 15 de clientes")
    for cliente in lista_top_clientes:
        print(f"{contador}. DNI {cliente[0]} gasto total: {cliente[1]}")
        contador += 1

def main():
    generar_vtos_2022()
    imprimir_vtos2022()
    imprimir_top_clientes()

main()