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
    vacunaciones = open(r"C:\Users\feden\Documents\Programación\repositorios git\fiuba\algoritmos y programacion I\prueba\vacunacion.csv", "r")
    advertencias = open(r"C:\Users\feden\Documents\Programación\repositorios git\fiuba\algoritmos y programacion I\prueba\advertencias.txt", "w")
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
    top_15 = lista_top_clientes[0:15]
    print(f"\nTop 15 de clientes")
    for cliente in top_15:
        print(f"{contador}. DNI {cliente[0]} gasto total: {cliente[1]}")
        contador += 1

def main():
    generar_vtos_2022()
    imprimir_vtos2022()
    imprimir_top_clientes()

main()