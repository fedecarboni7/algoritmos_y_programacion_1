# Escribir un programa modular, que solicite el ingreso de un valor, e informe si se trata de un número primo.

def num_primo(num):
    if(num == 1):
        return True
    else:
        for i in range(2, num):
            if (num % i == 0):
                break
        return(i+1 == num)


num = int(input("Ingresar numero natural: "))
if num_primo(num):
    print("Es primo")
else:
    print("No es primo")
