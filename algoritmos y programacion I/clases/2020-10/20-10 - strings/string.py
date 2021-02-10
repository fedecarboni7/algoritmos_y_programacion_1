#ejemplos de metodos con strings
palabra = "Algoritmo"
print(palabra[4])
print(palabra[-4:])
print(len(palabra)) #cantidad de caracteres
print(palabra.upper()) #convierte a mayuscula
print(palabra.count("o")) #cantidad de letras
print(palabra.index("t")) #devuelve la posición del caracter seleccionado
print(palabra.find("ori")) #devuelve la posición en la que comienza la subcadena, ó -1 si no está incluida
print(palabra.isalpha()) #devuelve true si esta compuesto por letras solamente
print(palabra.isnumeric()) #devuelve true si está compuesto por numeros solamente
print(palabra.isalnum()) #devuelve true si esta compuesto por letras y/o numeros

#mostrar el contenido de la variable palabra, imprimiendo un carácter por linea
for caracter in palabra:
    print(caracter)

#mostrar la cadena resultante de extraer las vocales de la variable palabra
for caracter in palabra:
    if(caracter.capitalize() not in "AEIOU"):
        print(caracter, end="")

#mostrar la cadena desde el último caracter al primero
for posicion in range(1, len(palabra)+1):
    print(palabra[-posicion], end="")

#alternativa
for posicion in reversed(range(len(palabra))):
    print(palabra[posicion], end="")
#alternativa2
print(palabra[::-1])