

givePaises = input("Ingrese Paises separados por comas ejemplo--> Alemania, Rusia, etc.\n")

listPaises  = givePaises.split(",")


set_Paises = {x for x in listPaises}

print(set_Paises)



