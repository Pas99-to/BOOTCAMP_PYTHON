'''En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis 
y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.'''


try:
    with open( "archivo.py" , "x" ) as f:
        f.write("#Create a new text FIle\n")
except FileExistsError:
    print("he documment txt already exist")

try:
    with open("archivo.py","a") as f:
        f.write("print('Hola Mundo')\n")
except FileNotFoundError:
    print("The documment not exist")