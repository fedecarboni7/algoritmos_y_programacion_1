linea = "4,50"

print(linea.rstrip("\n").split(","))

# .split(",") separa elementos en una lista cada vez que encuentra el valor pasado por parámetro
# .rstrip("\n") borra los valores pasados por parámetro que están a la derecha del string
# .lstrip() lo mismo que .rstrip() pero a la izquierda

diez = "10"
cinco = "5"
cuatro = "4"

men = min(int(cuatro), int(cinco), int(diez))

men = str(men)

print(men)

if int(diez) > int(cinco):
    print (diez)
else:
    print (cinco)