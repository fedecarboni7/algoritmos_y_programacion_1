class Curso:
    def __init__(self, nombre_curso, ):
       self.nombre_curso = ""
       self.alumnos = {}


    def definir_nombre(self):
        self.nombre_curso
        return


    def ingresar_alumnos(self, alumno, nota):
        self.alumnos += alumno
        self.alumnos[alumno] += nota
        return
    

    def cantidad_alumnos(self):
        return len(self.alumnos)
        

    def alumno_en_curso(self, alumno):
        return alumno in self.alumnos

    
curso_1 = Curso("Algo 1", )
