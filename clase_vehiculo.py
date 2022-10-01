
class Vehiculo:
    
    def vehiculo (self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class coche(Vehiculo):

    def coche(self,velocidad,cilidrada):
        self.velocidad = velocidad
        self.cilidrada = cilidrada

    def impresion(self):
        print("COLOR: ",self.color," RUEDAS: ",self.ruedas," Puertas: ",self.puertas," VELOCIDAD: ",self.velocidad," CILIDRADA: ",self.cilidrada)


coche_chico = coche()

coche_chico.vehiculo("Negro","4","4")
coche_chico.coche("250 km/h","2.5")
coche_chico.impresion()

