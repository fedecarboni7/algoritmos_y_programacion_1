'''
Ejercicio 2:
Modificar el programa anterior para que además de las 
condiciones anteriores la clave deba incluir al menos
un caracter numérico y  alguno de los siguientes caracteres especiales ‘#_&/()=’
'''
def ingresar_contraseña():
    print('''La palabra clave debe:
            1) contener por lo menos 10 caracteres
            2) debe tener un numero
            3) debe tener un caracter especial ‘#_&/()=’
            4) debe tener una letra mayúscula y una letra minúscula''')
    print('Si desea cancelar el ingreso de la misma debe ingresar Enter con cadena vacía')
    palabra = input('Ingrese la contraseña: ')
    return palabra


def validar_contraseña(palabra):

    if len(palabra) >= 10:

        tiene_mayusculas = False
        tiene_minusculas = False
        tiene_numero = False
        tiene_caracter_especial = False

        indice = 0

        while indice < len(palabra) and (not tiene_mayusculas or not tiene_minusculas or not tiene_numero or not tiene_caracter_especial):

            if palabra[indice] == palabra[indice].isalpha:
                if palabra[indice] == palabra[indice].upper():
                    tiene_mayusculas = True
                else:
                    tiene_minusculas = True
            elif palabra[indice] == palabra[indice].isnumeric():
                tiene_numero = True
            elif palabra[indice] in "#_&/()=":
                tiene_caracter_especial = True

            indice += 1

        if tiene_mayusculas and tiene_minusculas and tiene_numero and tiene_caracter_especial:

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

''' Resolucion:
# Escribir un programa, que permita el ingreso de una contraseña y la valide:
# La palabra clave debe contener por lo menos 10 caracteres
# Debe estar formada solo por caracteres alfabéticos, numéricos y por lo menos un caracter especial ‘#_&/()=’ 
# Al menos debe tener una letra mayúscula, una letra minúscula, un número y un caracter especial
# Si desea cancelar el ingreso de la misma debe ingresar Enter con cadena vacía

def ingresar_contraseña():
    print('La palabra clave debe contener por lo menos 10 caracteres')
    print('Debe estar formada solo por caracteres alfabéticos, numéricos y por lo menos un caracter especial "#_&/()="')
    print('Al menos debe tener una letra mayúscula, una letra minúscula, un número y un caracter especial')
    palabra = input('Ingrese la contraseña: ')
    return palabra

def validar_contraseña(palabra):
    
    if len(palabra) >= 10:
        
        es_valida = True
        
        tiene_mayusculas = False
        tiene_minusculas = False
        tiene_numeros    = False
        tiene_especial   = False
        
        indice = 0
        
        while indice < len(palabra) and es_valida:
            
            if palabra[indice].isalpha():
                
                if palabra[indice] == palabra[indice].upper():
                    tiene_mayusculas = True
                else:
                    tiene_minusculas = True
                    
            elif palabra[indice].isnumeric():
                
                tiene_numeros = True
                
            elif palabra[indice] in '#_&/()=':
            
                tiene_especial = True
                    
            else:
                es_valida = False
                
            indice += 1
                
        if es_valida:
            
            if not tiene_mayusculas or not tiene_minusculas or not tiene_numeros or not tiene_especial:
                
                es_valida = False
        
        
    else:
        es_valida = False
        
    return es_valida

def main():
    
    contraseña = ingresar_contraseña()
    
    while len(contraseña) > 0 and not validar_contraseña(contraseña):
        
        print('La contraseña ingresada no cumple con los requisitos pedidos, por favor reingresela')
        
        contraseña = ingresar_contraseña()
        
    if len(contraseña) > 0:
        
        print('La contraseña se genero en forma exitosa')
      
    return

main()
'''