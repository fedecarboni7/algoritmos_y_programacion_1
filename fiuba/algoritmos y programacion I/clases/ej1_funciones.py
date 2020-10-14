"""Solicitar el ingreso de un número, calcular su factorial y luego informarlo.
Tener en cuenta que el factorial de un número N, entero positivo, es el producto de todos los números enteros
positivos desde 1 hasta N; y que el factorial de 0, es 1. Si el usuario ingresa un valor menor a cero, se debe
mostrar un mensaje que diga que no es factible calcular el factorial de dicho número."""


def ingresar_num():
    num = int(input("Ingresar numero:"))
    while(num < 0):
        print("No se permiten numeros negativos")
        num = int(input("Ingresar numero:"))
    return num


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact


print("El factorial del numero ingresado es:", factorial(ingresar_num()))
