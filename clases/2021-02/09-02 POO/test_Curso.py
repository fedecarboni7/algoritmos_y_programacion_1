import unittest
from Curso import Curso

class TestCurso(unittest.TestCase):
    def test_agrego_un_alumno_y_este_se_encuentra_en_el_curso(self):
        curso = Curso("Guarna", "Juarez")
        
        curso.ingresarAlumnoConNota("Uriel", 10)
        
        self.assertTrue(curso.alumnoEstaEnCurso("Uriel"))
        
    def test_agrego_un_alumno_y_este_se_encuentra_en_el_curso_bis(self):
        curso = Curso("Guarna", "Juarez")
        
        self.assertTrue(curso.alumnoEstaEnCurso("Uriel"))
    
if __name__ == '__main__':
   unittest.main()
