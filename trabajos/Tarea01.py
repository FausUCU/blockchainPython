
name=input("write your name: ")
age=input("write your age: ")


def inpresor1():
    temp=name+age
    print(temp)
def inpresor2():
    primerS=input("write the first word: ")
    segundaS=input("write the second word: ")
    print(primerS+segundaS)
def calEdad(Age):
    decadas=Age//10
    return decadas 

#test function
inpresor1()
inpresor2()
nombre2=input("write your name: ")
edad2=int(input("write your age: "))
decada=calEdad(edad2)
print(nombre2+ " has lived for " +str(decada)+" decades")
#test function End

'''
Esto sirve para comentar a lo largo, usa este # symbolo
para solo el renglon, la tecal de comillas es el simbolo de interrogacion
'''