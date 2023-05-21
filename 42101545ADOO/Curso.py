class Materia:
    def __init__(self, clave:int, nombre:str, semestre:str, creditos:int, profesor:Profesor):
        self.clave = clave
        self.nombre = nombre
        self.semestre = semestre
        self.creditos = creditos
        self.profesor = profesor
    
    def add_profesor(self, profesor:Profesor):
        self.profesor = profesor
