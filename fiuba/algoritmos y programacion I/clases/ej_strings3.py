'''
Ejercicio 3:
Escribir otro programa, que permita el ingreso de una contraseña y la valide:
La palabra clave debe contener por lo menos 10 caracteres
Debe estar formada solo por caracteres alfabéticos y números.
Al menos debe tener una letra mayúscula, una letra minúscula y un número.
En caso que la contraseña ingresada no sea válida debe mostrar los motivos por los cuales debe volver a re-ingresarla.
Si desea cancelar el ingreso de la misma debe ingresar Enter con cadena vacía
'''
def ingresar_contraseña():
    print('La palabra clave debe estar formada por caracteres alfabéticos y números')
    print('Al menos debe tener una mayúsculas, una minúscula y un número')
    print('Si desea finalizar presione enter')
    contraseña = input('Ingrese la contraseña: ')
    return contraseña

def validar_contraseña(contraseña):
    
    if len(contraseña) >= 10:        
        longitud = True
    else:
        longitud = False
    
    tiene_mayusculas = False
    tiene_minusculas = False
    tiene_numeros    = False
    tiene_otros      = False
  
    for caracter in contraseña:
            
        if caracter.isalpha():
            if caracter == caracter.upper():
                tiene_mayusculas = True
            else:
                tiene_minusculas = True
        elif caracter.isnumeric():
            tiene_numeros = True
        else:
            tiene_otros = True
                
    return (longitud, tiene_mayusculas, tiene_minusculas, tiene_numeros, tiene_otros)

def mostrar_motivo(longitud, tiene_mayusculas, tiene_minusculas, tiene_numeros, tiene_otros):
    if not longitud:
        print('La palabra ingresada no cumple con la longitud de 10 caracteres')
    if not tiene_mayusculas:
        print('La palabra ingresada no tiene letras mayúsculas')
    if not tiene_minusculas:
        print('La palabra ingresada no tiene letras minúsculas')
    if not tiene_numeros:
        print('La palabra ingresada no tiene numeros')
    if tiene_otros:
        print('La palabra ingresada tiene caracteres especiales')
    return

def main():
    
    contraseña = ingresar_contraseña()
    longitud, mayusculas, minusculas, numeros, otros = validar_contraseña(contraseña)
    
    while len(contraseña) > 0 and ( not longitud or not mayusculas or not numeros or otros ):
                
        mostrar_motivo(longitud, mayusculas, minusculas, numeros, otros)

        contraseña = ingresar_contraseña()
        longitud, mayusculas, minusculas, numeros, otros = validar_contraseña(contraseña)
        
    if len(contraseña) > 0:
        print('La contraseña se generó exitosamente')
    else:
        print('No se generó la contraseña')
    return

main()