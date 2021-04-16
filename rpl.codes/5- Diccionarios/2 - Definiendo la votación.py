def solicitar_valor(mensaje):
    valor = input(mensaje)
    return valor


def cargar_tabla():
    seguir = "s"
    tabla = {}
    while seguir == "s":
        partido = solicitar_valor("Ingrese el partido a sumarle votos: ")
        votos = int(solicitar_valor(
            "Ingrese la cantidad de votos a sumarle: "))
        if partido not in tabla:
            tabla[partido] = votos
        else:
            tabla[partido] += votos
        seguir = solicitar_valor("Desea seguir ingresando?(s/n): ")
    return tabla


def ordenar_tabla(t):
    lista_tabla = t.items()
    return sorted(lista_tabla, key=lambda l: l[1], reverse=True)


def mostrar_resultados(resultados):
    for partido, votos in resultados:
        print(f"El partido {partido} obtuvo {votos} votos.")


t = cargar_tabla()
resultados = ordenar_tabla(t)
mostrar_resultados(resultados)
