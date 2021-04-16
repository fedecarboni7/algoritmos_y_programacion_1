"""Escribir un programa en Python que solicite el ingreso de un número que representa un mes, y luego informe de que mes se trata.
Si el número no representa ningún mes, enviar el mensaje "Mes Inválido"""""
mes = int(input("Ingrese numero de mes:"))
if (mes == 1):
    print("Enero")
elif(mes == 2):
    print("Febrero")
elif(mes == 3):
    print("Marzo")
elif(mes == 4):
    print("Abril")
elif(mes == 5):
    print("Mayo")
elif(mes == 6):
    print("Junio")
elif(mes == 7):
    print("Julio")
elif(mes == 8):
    print("Agosto")
elif(mes == 9):
    print("Septiembte")
elif(mes == 10):
    print("Octubre")
elif(mes == 11):
    print("Noviembre")
elif(mes == 12):
    print("Diciembre")
else:
    print("Mes invalido")
    
