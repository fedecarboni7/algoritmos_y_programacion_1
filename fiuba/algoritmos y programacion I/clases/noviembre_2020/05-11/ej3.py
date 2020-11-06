def solicitar_valor(mensaje):
    valor = input(mensaje)
    return valor


def cargar_tabla():
    partido = solicitar_valor("Cargar partido: ")
    if partido != "no":
        votos = int(solicitar_valor("Cargar votos: "))
        tabla = {}
        while partido != "no":
            if partido not in tabla:
                tabla[partido] = votos
            else:
                tabla[partido] += votos
            partido = solicitar_valor("Cargar partido: ")
            if partido != "no":
                votos = int(solicitar_valor("Cargar votos: "))
    return tabla


def ordenar_tabla(t):
    lista_tabla = t.items()
    print(sorted(lista_tabla, key=lambda l: l[1], reverse=True))


t = cargar_tabla()
ordenar_tabla(t)
