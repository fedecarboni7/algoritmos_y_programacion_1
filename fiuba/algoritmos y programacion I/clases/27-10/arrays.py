lista = [1,2,3,4,"azul","camion",34.2]
lista += [0,12,23,34]

lista[2] = 45 #asigna un valor a la posiscion seleccionada de la lista

#Funciones con listas
lista.append(-23) #agrega un valor al final de la lista

lista.extend(range(4)) #agrega elementos de un iterable al final de la lista

lista.insert(1, "hola") #inserta un valor en la posicion 1 y mueve el resto una posicion atras

del(lista[0]) #elimina el valor de la posicion 0

print(lista.pop(-2)) #elimina el anteultimo elemento y lo muestra
print(lista.pop(0)) #elimina el primer elemento y lo muestra

lista.remove("camion") #elimina el valor seleccionado (en caso de repetirse, el primero que encuentra)

#lista.clear() #elimina todos los elementos

print(lista.count(0)) #cuenta la cantidad de veces que aparece el cero

lista.reverse() #revierte los elementos de la lista

lista2 = [0,23,32,3,4,-324,-3]
lista2.sort() #ordena la lista sobre si misma

ord_lista2 = sorted(lista2) #ordena la lista sin afectar a la original
print(ord_lista2)

print(lista)

print(len(lista)) #muestra la cantidad de elementos de la lista

lista_vacia = []
print(len(lista_vacia))

#para acceder a partes de una lista
print(lista[0:4])
print(lista[2:])

#para elimninar un parte especifica de la lista
lista3 = ["primer",1,2,3,4,5,6,7]

lista3[2:4] = []
# o sino:
del(lista3[5:7])

print(lista3)

#listas que contienen listas
l_super = [["jabon", 3], ["aguas", 4], ["latas", 2]]
#para acceder a cantidad de latas
print(l_super[2][1])

notas_alumnos = [["Federico", [6,9,7]], ["Gabriel",[5,10]]]
#segunda nota de Federico
print(notas_alumnos[0][1][1])