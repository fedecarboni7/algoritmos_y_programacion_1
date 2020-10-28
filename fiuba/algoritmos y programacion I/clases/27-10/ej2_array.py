#generar una lista que contenga los cuadrados de los numeros del 1 al 100
lista = []

for i in range(1,101):
    lista += [i**2]

print(lista)

#lista por comprension
lista2 = [x ** 2 for x in range(1,101)]
print(lista2)