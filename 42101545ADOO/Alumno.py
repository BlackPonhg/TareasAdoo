class Alumno:
    def __init__(self, nombre, apaterno, amaterno, email):
        self.nombre = nombre
        self.apaterno = apaterno
        self.amaterno = amaterno
        self.email = email
        
    def matricula(self, codigo):
        if len(codigo) == 10:
            self.codigo = codigo
            print(f"El alumno {self.nombre} se ha matriculado con el código {self.codigo}")
        else:
            print("El código de matrícula debe tener 10 caracteres.")
