from unicodedata import name
#comentarion


nombre="original"
print("el nombre original es: "+nombre)
def modificar():
    nombre=(input("Ingrese un nombre: "))
modificar()
print(" el nombre sin modificar global es "+nombre)
def modificarGlobal():
    global nombre 
    nombre = input("Ingrese un nombre: ")

modificarGlobal()

print(" el nombre con modificar global es "+nombre)
    