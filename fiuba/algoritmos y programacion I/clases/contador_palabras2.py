def cant_palabras(cadena):
    """
    >>> cant_palabras("La  tierra es redonda  y el sol   amarillo")
    8
    >>> cant_palabras("La luna es  un satelite    natural que  gira alrededor de la tierra")
    12
    >>> cant_palabras("     ")
    0
    >>> cant_palabras("Marte y Jupiter forman parte de nuestro sistema solar")
    9
    """
    cantidad_palabras = 0
    comienzo_palabra = False
    for caracter in cadena:
        if caracter != ' ' and not comienzo_palabra:
            comienzo_palabra = True
            cantidad_palabras += 1
        elif caracter == ' ' and comienzo_palabra:
            comienzo_palabra = False
    return cantidad_palabras

#-------------------- Bloque Principal --------------------#
import doctest
print(doctest.testmod())
    