
class Alumno:

    def __init__(self,nombre,_nota) -> None:
        self.nombre=nombre
        self.nota=_nota
        print("ALUMNO: ", self.nombre," NOTA: ",self.nota, "ESTATUS: ", self.apropadoOrReprobado())
    
    def notaS(self):
        return self.nota
    

    def apropadoOrReprobado(self):
         if self.notaS() <= 6:
            return "Reprobado"
         elif self.notaS() > 6:
            return "Aprobado"
         else:
            return "Nota desconocida" 

alum = Alumno('Roberto',8)