def validar_contrasenia(contrasenia):

    if 7 < len(contrasenia) < 15:

        es_valida = True

        tiene_mayusculas = False
        tiene_minusculas = False
        tiene_numero = False
        tiene_caracter_especial = False

        indice = 0

        while indice < len(contrasenia) and es_valida:

            if contrasenia[indice].isalpha():
                if contrasenia[indice] == contrasenia[indice].upper():
                    tiene_mayusculas = True
                else:
                    tiene_minusculas = True
            elif contrasenia[indice].isnumeric():
                tiene_numero = True
            elif not (contrasenia[indice].isalpha() and contrasenia[indice].isnumeric()):
                tiene_caracter_especial = True
            else:
                es_valida = False

            indice += 1

        if es_valida:

            if not tiene_mayusculas or not tiene_minusculas or not tiene_numero or not tiene_caracter_especial:

                es_valida = False

    else:

        es_valida = False

    return es_valida
