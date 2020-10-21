# tu codigo
lado1 = int(input("Ingrese la longitud del primer lado del triangulo: "))
lado2 = int(input("Ingrese la longitud del segundo lado del triangulo: "))
lado3 = int(input("Ingrese la longitud del tercer lado del triangulo: "))
if(lado1 == lado2 == lado3):
    print("Es equilatero")
elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print("Es isosceles")
else:
    print("Es escaleno")