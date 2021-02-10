class Curso:
    cantidad_de_cursos = 0

    def __init__(self, nombre_titular, nombre_jtp):
        self.nombre_titular = nombre_titular
        self.nombre_jtp = nombre_jtp
        self.alumnos = {}
        Curso.cantidad_de_cursos += 1

    def titulares_catedra(self):
        return self.nombre_titular, self.nombre_jtp

    def ingresar_alumnos_con_nota(self, alumno, nota):
        self.alumnos[alumno] = nota
        return
    
    def nota_alumno(self, alumno):
        if self.alumno_en_curso(alumno):
            return self.alumnos[alumno]
        else:
            raise Exception("El alumno no se encuentra en el curso")

    def cantidad_alumnos(self):
        return len(self.alumnos)

    def alumno_en_curso(self, alumno):
        return alumno in self.alumnos


curso_guarna = Curso("Pablo Guarna", "Juarez")

print(curso_guarna.cantidad_alumnos())

curso_guarna.ingresar_alumnos_con_nota("Uriel", 10)
curso_guarna.ingresar_alumnos_con_nota("Augusto", 2)
curso_guarna.ingresar_alumnos_con_nota("Matias", 8)
curso_guarna.ingresar_alumnos_con_nota("Andres", 2)

print(curso_guarna.alumno_en_curso("Matias"))
print(curso_guarna.alumno_en_curso("Tomas"))

print("Cantidad de alumnos: ", curso_guarna.cantidad_alumnos())

print(curso_guarna.nota_alumno("Uriel"))

curso_andy = Curso("Juarez", "Perez")

print(curso_andy.cantidad_alumnos())
print(curso_andy.cantidad_de_cursos)
