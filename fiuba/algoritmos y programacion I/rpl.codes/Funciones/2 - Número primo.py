def es_primo(numero):
    #tu codigo
    if(numero == 1 or numero == 2):
        condicion = True
    else:
        for i in range(2, numero):
            if (numero % i == 0):
                break
        if (i+1 == numero):
            condicion = True
        else:
            condicion = False
    return condicion