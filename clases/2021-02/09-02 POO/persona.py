class Persona():
    altura = 1.50

    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def crecer_un_centrimetro(self):
        self.altura += 0.01

    def crecer_un_año(self):
        self.edad += 1


persona = Persona("Juan Perez", 22, 1.80)

persona.crecer_un_centrimetro()
persona.crecer_un_año()

print(persona.nombre)
print(persona.edad)
print(persona.altura)

persona2 = Persona("Micaela Sochan", 20, 1.68)

print(persona2.nombre)
print(persona2.edad)
print(persona2.altura)
