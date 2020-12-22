def numeros_positivos(numero):
    return [x for x in range(1, numero+1)]


def numeros_positivos_pares(numero):
    return [x for x in range(2, numero+1, 2)]


def numeros_positivos_pares_cuadrado(numero):
    return [x**2 for x in range(2, numero+1, 2)]


def impares_al_cuadrado(lista):
    return [x if x % 2 == 0 else x**2 for x in lista]


def filtrar_tuplas_por_suma(lista_de_tuplas):
    return [lista_de_tuplas[x] for x in range(len(lista_de_tuplas)) if lista_de_tuplas[x][0] + lista_de_tuplas[x][1] >= 0]


def filtrar_tupla_elemento_par(lista_de_tuplas):
    return [lista_de_tuplas[x] for x in range(len(lista_de_tuplas)) if lista_de_tuplas[x][0] % 2 == 0 or lista_de_tuplas[x][1] % 2 == 0]
