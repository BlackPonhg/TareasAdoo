from profesor import Profesor
from examen import Examen

class Grupo:
    def __init__(self, clave:int, nombre:str, semestre:str, creditos:int, profesor:Profesor):
        self.clave = clave
        self.nombre = nombre
        self.semestre = semestre
        self.creditos = creditos
        self.profesor = profesor
        self.alumnos = []
        self.materias = []
        self.asistencia = {}
    
    def add_alumno(self, alumno:Alumno):
        self.alumnos.append(alumno)
        
    def add_materia(self, materia:Materia):
        self.materias.append(materia)
        
    def lista_asistencia(self):
        return self.asistencia
    
    def aplica_examen(self, alumno:Alumno, examen:Examen, materia:Materia):
        if examen.activo:
            if materia in alumno.materias:
                if alumno in self.alumnos:
                    if alumno not in self.asistencia:
                        self.asistencia[alumno] = {}
                    if materia not in self.asistencia[alumno]:
                        self.asistencia[alumno][materia] = []
                    self.asistencia[alumno][materia].append(examen)
                    alumno.calificaciones[materia][examen.nombre] = examen.aciertos
                    return True
        return False
