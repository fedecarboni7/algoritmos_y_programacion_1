def raiz(num, error):
    piso = 1
    techo = num
    calc = (techo - piso) / 2
    diferencia = abs((calc * calc) - num)
    while(diferencia > error):
        if(calc * calc > num):
            techo = calc
        else:
            piso = calc
        calc = (techo + piso) / 2
        diferencia = abs((calc * calc) - num)
    return calc


def main():
    print("")
    num = int(input("Ingrese valor: "))
    error = float(input("Ingrese valor de error a tolerar: "))
    print("La raíz cuadrada de", num, "es:", raiz(num, error))


#main()
