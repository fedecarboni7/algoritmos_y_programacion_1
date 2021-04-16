dia = int(input("Ingrese numero de día:"))
mes = int(input("Ingrese numero de mes:"))
if (mes == 1):
    calculo = dia
elif (mes == 2):
    calculo = ((mes-1)*31) + dia
elif (mes == 3):
    calculo = ((mes-1)*31) - 3 + dia
elif (mes == 4):
    calculo = ((mes-1)*31) - 3 + dia
elif (mes == 5):
    calculo = ((mes-1)*31) - 4 + dia
elif (mes == 6):
    calculo = ((mes-1)*31) - 4 + dia
elif (mes == 7):
    calculo = ((mes-1)*31) - 5 + dia
elif (mes == 8):
    calculo = ((mes-1)*31) - 5 + dia
elif (mes == 9):
    calculo = ((mes-1)*31) - 5 + dia
elif (mes == 10):
    calculo = ((mes-1)*31) - 6 + dia
elif (mes == 11):
    calculo = ((mes-1)*31) - 6 + dia
elif (mes == 12):
    calculo = ((mes-1)*31) - 7 + dia
print("Estas en el dia N°",calculo,"del año")