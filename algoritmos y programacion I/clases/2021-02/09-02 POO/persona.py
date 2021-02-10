class Persona():
   altura = 1.50
   def __init__(self, nombre, edad, altura):
       self.nombre = nombre
       self.edad = edad
       self.altura = altura

   def crecer_un_centrimetro(self):
       self.altura += 0.01


persona = Persona("Juan Perez", 22, 1.80)

persona.crecer_un_centrimetro()