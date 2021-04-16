"""
Un supermercado con dos sucursales tiene a fin de mes generados dos archivos 
VENTAS_1.CSV y VENTAS_2.CSV que tienen el siguiente formato:

dia(DD),nro_caja(NN),legajo_vendedor,monto_recaudado

Los archivos estan ordenados en forma creciente por di­a y, a igual dia, por numero de caja. 
Ademas guardan la recaudacion por cambio de vendedor, por lo que para un mismo dia y una misma caja 
puede haber mas de un registro.

Se pide hacer un programa modularizado en Python que, leyendo una sola vez cada archivo:

a) Genere un archivo unificado conservando el orden (a igual di­a y numero de caja guardar primero los de la sucursal 1). Listo

b) En base al archivo generado en el punto anterior y sin utilizar estructuras adicionales, 
imprima un informe indicando los totales diarios:

Dia DD: monto recaudado: XXX

c) Indique el legajo del vendedor que mas recaudo (para este punto se pueden utilizar estructuras auxiliares).
"""
# constantes
MAX_DIA = "999"


def leer_archivo(archivo):
    linea = archivo.readline()
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        registro = [MAX_DIA, '', '', '']  # Condición de salida del while
    return registro


def merge_archivos():
    ventas_1 = open("C:\\Users\\feden\\Documents\\Programación\\repositorios git\\fiuba\\algoritmos y programacion I\\examenes\\modelos_de_finales\\final_1\\ventas_1.csv", "r")
    ventas_2 = open("C:\\Users\\feden\\Documents\\Programación\\repositorios git\\fiuba\\algoritmos y programacion I\\examenes\\modelos_de_finales\\final_1\\ventas_2.csv", "r")
    ventas = open("C:\\Users\\feden\\Documents\\Programación\\repositorios git\\fiuba\\algoritmos y programacion I\\examenes\\modelos_de_finales\\final_1\\ventas.csv", "w")

    dia_1, caja_1, legajo_1, monto_1 = leer_archivo(ventas_1)
    dia_2, caja_2, legajo_2, monto_2 = leer_archivo(ventas_2)

    while dia_1 != MAX_DIA or dia_2 != MAX_DIA:

        dia_menor = min(dia_1, dia_2)
        caja_menor = min(caja_1, caja_2)

        while dia_1 == dia_menor and caja_1 == caja_menor:
            ventas.write(dia_1 + "," + caja_1 + "," + legajo_1 + "," + monto_1 + "\n")
            dia_1, caja_1, legajo_1, monto_1 = leer_archivo(ventas_1)

        while dia_2 == dia_menor and caja_2 == caja_menor:
            ventas.write(dia_2 + "," + caja_2 + "," + legajo_2 + "," + monto_2 + "\n")
            dia_2, caja_2, legajo_2, monto_2 = leer_archivo(ventas_2)

        while dia_1 == dia_menor and caja_1 > caja_menor:
            ventas.write(dia_1 + "," + caja_1 + "," + legajo_1 + "," + monto_1 + "\n")
            dia_1, caja_1, legajo_1, monto_1 = leer_archivo(ventas_1)

        while dia_2 == dia_menor and caja_2 > caja_menor:
            ventas.write(dia_2 + "," + caja_2 + "," + legajo_2 + "," + monto_2 + "\n")
            dia_2, caja_2, legajo_2, monto_2 = leer_archivo(ventas_2)

    ventas_1.close
    ventas_2.close
    ventas.close


def totales_diarios():
    ventas = open(
        "C:\\Users\\feden\\Documents\\Programación\\repositorios git\\fiuba\\algoritmos y programacion I\\examenes\\ventas.csv", "r")

    dia, caja, legajo, monto = leer_archivo(ventas)
    dicc_legajos = {legajo: 0}

    while dia != MAX_DIA:
        dia_menor = dia
        monto_recaudado = 0

        while dia == dia_menor:
            monto_recaudado += int(monto)
            if legajo in dicc_legajos:
                dicc_legajos[legajo] += int(monto)
            else:
                dicc_legajos[legajo] = int(monto)
            
            dia, caja, legajo, monto = leer_archivo(ventas)
            
        print(f"\nDia {dia_menor}: monto recaudado: {monto_recaudado}")

    print("\nEl legajo que más recaudó fue el:")
    print(max(dicc_legajos))

    ventas.close


def main():
    merge_archivos()
    totales_diarios()


main()
