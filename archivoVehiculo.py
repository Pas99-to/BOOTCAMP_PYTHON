'''En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase 
Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.'''

from fileinput import close


file = open("vehiculo.py","w")
file.write("\n\n")
file.write("class Vehiculo:\n")  
file.close()

file = open("vehiculo.py","a")
file.write("    def __init__(self, marca, placa):\n")
file.write("        self.marca=marca\n")
file.write("        self.placa=placa\n")

file.write("carro = Vehiculo('Nissan','G7R4423')\n")
file.write("print(carro.marca)\n")
file.write("print(carro.placa)\n")

file.close()



