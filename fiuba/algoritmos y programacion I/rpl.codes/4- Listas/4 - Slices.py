def ultimos_tres_elementos(lista):
    return lista[-3:]


def ultimos_tres_elementos_concatenados(lista):
    lista2 = []
    for i in lista:
        lista2 += i[-3:]
    return lista2


def indices_pares(lista):
    return [lista[i] for i in range(0, len(lista), 2)]


def indices_impares(lista):
    return [lista[i] for i in range(1, len(lista), 2)]


def invertir(lista):
    lista.reverse()
    return lista
