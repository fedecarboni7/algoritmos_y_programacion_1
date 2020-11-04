'''
Escribir una función en Python que reciba una cadena de caracteres
y devuelva la cantidad de palabras que hay.
La cadena recibida solo estara compuesta por letras y blancos.
Considerar que las palabras están separadas por uno ó más blancos.

Pruebe con los siguientes ejemplos:
    "La  tierra es redonda  y el sol   amarillo"
    "La luna es  un satelite    natural que  gira alrededor de la tierra"
    "     "
    "Marte y Jupite forman parte de nuestro sistema solar"

'''
def palabras():
    cadenaPalabras = input("Ingresar cadena de palabras:")
    listaPalabras = cadenaPalabras.split()
    return(listaPalabras)
print(palabras())