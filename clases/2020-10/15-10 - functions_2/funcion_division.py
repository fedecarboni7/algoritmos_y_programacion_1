def division(dividendo, divisor):
    for cociente in range(1, dividendo + 1):
        resto = dividendo - (divisor * cociente)
        if(resto < divisor):
            break
    return cociente


def main():
    print("")
    dividendo = int(input("Ingrese valor de dividendo: "))
    divisor = int(input("Ingrese valor de divisor: "))
    print(dividendo, "dividido", divisor, "es:",division(dividendo, divisor))


#main()
