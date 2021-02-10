class Curso:
    cantidadDeCursos = 0
    
    def __init__(self, nombreTitular, nombreJtp):
        self.nombreTitular = nombreTitular
        self.nombreJtp = nombreJtp
        self.alumnos = {}
        Curso.cantidadDeCursos += 1
        
    def titularesCatedra(self):
        return self.nombreTitular, self.nombreJtp
    
    def configurarNombre(self, nombre):
        self.nombre = nombre
        
    def ingresarAlumnoConNota(self, nombreAlumno, nota):
        self.alumnos[nombreAlumno] = nota
        
    def cantidadDeAlumnos(self):
        return len(self.alumnos)
    
    def alumnoEstaEnCurso(self, alumno):
        return alumno in self.alumnos
    
    def notaDeAlumno(self, alumno):
        if self.alumnoEstaEnCurso(alumno):
            return self.alumnos[alumno]
        else:
            raise Exception("El alumno no se encuentra en el curso")
    
    def cantidadDeCursosRegistrados(self):
        return Curso.cantidadDeCursos

cursoDePablo = Curso("Guarna", "Juarez")

print(cursoDePablo.cantidadDeAlumnos())

cursoDePablo.ingresarAlumnoConNota("Uriel", 10)
cursoDePablo.ingresarAlumnoConNota("Augusto", 2)
cursoDePablo.ingresarAlumnoConNota("Matias", 8)
cursoDePablo.ingresarAlumnoConNota("Andres", 2)

print(cursoDePablo.alumnoEstaEnCurso("Matias"))
print(cursoDePablo.alumnoEstaEnCurso("Tomas"))

print("Cantidad de alumnos: ", cursoDePablo.cantidadDeAlumnos())

print(cursoDePablo.notaDeAlumno("Uriel"))

cursoDeAndy = Curso("Juarez", "Perez")

print(cursoDeAndy.cantidadDeAlumnos())
print(cursoDeAndy.cantidadDeCursosRegistrados())
