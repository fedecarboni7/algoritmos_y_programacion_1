"""
Ejercicio 1:
Escribir un programa, que permita el ingreso de una contraseña y la valide:
La palabra clave debe contener por lo menos 10 caracteres
Debe estar formada solo por caracteres alfabéticos
Al menos debe tener una letra mayúscula y una letra minúscula
Si desea cancelar el ingreso de la misma debe ingresar Enter con cadena vacía
"""


def ingresar_contraseña():
    print('''La palabra clave debe:
            1) contener por lo menos 10 caracteres
            2) debe estar formada solo por caracteres alfabéticos
            3) debe tener una letra mayúscula y una letra minúscula''')
    print('Si desea cancelar el ingreso de la misma debe ingresar Enter con cadena vacía')
    palabra = input('Ingrese la contraseña: ')
    return palabra


def validar_contraseña(palabra):

    if len(palabra) >= 10 and palabra.isalpha():

        tiene_mayusculas = False
        tiene_minusculas = False

        indice = 0

        while indice < len(palabra) and (not tiene_mayusculas or not tiene_minusculas):

            if palabra[indice] == palabra[indice].upper():
                tiene_mayusculas = True
            else:
                tiene_minusculas = True

            indice += 1

        if tiene_mayusculas and tiene_minusculas:

            es_valida = True

        else:

            es_valida = False

    else:

        es_valida = False

    return es_valida


def main():

    contraseña = ingresar_contraseña()

    while len(contraseña) > 0 and not validar_contraseña(contraseña):

        contraseña = ingresar_contraseña()

    if len(contraseña) > 0:

        print('La contraseña se genero en forma exitosa')

    return


main()
