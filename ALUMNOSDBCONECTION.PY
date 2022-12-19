import sqlite3

#DOING CONECTION WITH DATABASE
def conection():
   conn = sqlite3.connect('ESCUELA.DB',isolation_level=None) 
   return conn

#GET DATA THERRE ARE INSIDE DATA BASE
def getData():
   return conection().execute("SELECT * FROM Alumno")

#INSERT DATA INSIDE DATABASE
def insertDB():
   conexión = conection().cursor()
   nombre = str(input("Ingrese Nombre del Estudiante: "))
   apellido = str(input("Ingrese Apellido del EStudiante: "))
   conexión.execute("INSERT INTO Alumno(NOMBRE, APELLIDO) VALUES(:nom, :ape)",{'nom':nombre,'ape':apellido})

#SEARCH STUDENTS INSIDE DATABASE FOR NAME 
def searchStudent():
   conexión =conection().cursor()
   nombre = str(input("Ingrese nombre del Alumno: "))
   return conexión.execute("SELECT * FROM Alumno WHERE NOMBRE = :nombre",{'nombre':nombre})

#TO CHOOSE A OPTION 
def menuOptions():
   
   flag = True
   while flag:   
      option = input("Digite: \n (1)Insertar Dato \n (2)Buscar Dato \n (3)Salir \n")
      match option:
         case "1":
            insertDB()
         case "2":
            for row in searchStudent():
               print ("\nID = ", row[0])
               print ("NOMBRE = ", row[1])
               print ("APELLIDO = ", row[2]+"\n")
         case "3":
             flag = False
             conection().close()

menuOptions()