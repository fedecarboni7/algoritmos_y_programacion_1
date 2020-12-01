'''Se pide construir un programa que nos permita obtener estadísticas del mercado laboral 
por localidad con el fin de poder realizar comparaciones.

Para comenzar, se deben comenzar cargando en un diccionario pares de datos localidad-personas, 
donde el valor de las personas hace referencia a la cantidad de personas que se encuentra en edad de trabajar.
Debe tenerse en cuenta que, como los datos se obtienen de distintas planillas, es posible que se ingrese más de 
un par clave-valor asociada a una localidad.

Una vez que el usuario terminar de realizar la carga, se deben imprimir:

a) El total de personas en edad laboral y el total de empleados para cada localidad.

b) Un listado ordenado de mayor a menor por porcentaje de desocupación. Debe tenerse
   en cuenta que para determinar el porcentaje de desocupación se puede utilizar la fórmula:

% desocupacion = (1 - empleados / personas en edad de trabajar) * 100

'''


def solicitar_valor(mensaje):
    valor = input(mensaje)
    return valor


def cargar_diccionario():
    mercado_laboral = {}
    seguir = "s"
    while seguir == "s":
        localidad = solicitar_valor("Ingrese localidad: ")
        personas_mayores = int(solicitar_valor("Ingrese la cantidad de personas que pueden trabajar: "))
        empleados = int(solicitar_valor("Ingrese la cantidad de empleados: "))
        if localidad not in mercado_laboral:
            mercado_laboral[localidad] = [personas_mayores, empleados, 0]
        else:
            mercado_laboral[localidad][0] += personas_mayores
            mercado_laboral[localidad][1] += empleados
        desocupacion = (1 - mercado_laboral[localidad][1] / mercado_laboral[localidad][0]) * 100
        mercado_laboral[localidad][2] = desocupacion
        seguir = solicitar_valor("Desea seguir ingresando?(s/n): ")
    return mercado_laboral


def mostrar_estadisticas(lista):
    for localidad, datos in lista:
        personas_mayores = datos[0]
        empleados = datos[1]
        print(f"En la localidad de {localidad} hay {personas_mayores} personas en edad laboral y {empleados} trabajando.")
    return


def ordenar_por_desocupacion(dicc):
    lista_market = dicc.items()
    return sorted(lista_market, key=lambda l: l[1][2], reverse=True)


def mostrar_desocupacion(lista):
    for localidad, datos in lista:
        desocupacion = datos[2]
        print(f"La tasa de desocupacion en {localidad} es {desocupacion:.1f}%.")
    return


dicc = cargar_diccionario()
mostrar_estadisticas(dicc.items())
mostrar_desocupacion(ordenar_por_desocupacion(dicc))
