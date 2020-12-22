def ordenar_lista_menor_a_mayor(lista):
    return sorted(lista)


def ordenar_lista_mayor_a_menor(lista):
    return sorted(lista, reverse=True)


def ordenar_lista_alfabeticamente(lista):
    return sorted(lista)


def ordenar_palabras_por_longitud(lista):
    return sorted(lista, key=lambda i: len(i), reverse=True)


def ordenar_lista_por_tupla(lista):
    return sorted(lista, key=lambda i: i[1], reverse=True)


def ordenar_lista_por_suma_tupla(lista):
    return sorted(lista, key=lambda i: i[0] + i[1], reverse=True)
