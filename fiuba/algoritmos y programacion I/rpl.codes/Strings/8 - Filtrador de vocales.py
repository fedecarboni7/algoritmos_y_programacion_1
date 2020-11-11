def filtrador_de_vocales(cadena):
    consonantes = ""
    for caracter in cadena:
        if(caracter not in "aeiou"):
            consonantes += caracter
    return consonantes