def es_primo(numero):
    # tu codigo
    condicion = False
    if(numero == 2):
        condicion = True
    elif(numero > 2):
        for i in range(2, numero):
            if (numero % i == 0):
                break
        if (i+1 == numero):
            condicion = True
    return condicion
