"""Escribir un programa modular, que solicite el ingreso de un valor, e informe si se trata de un número primo."""
num = 991
for i in range(2, num):
  if (num%i == 0):
    break
if (i+1 == num):
  print("es primo")
else:
 print("no es primo")