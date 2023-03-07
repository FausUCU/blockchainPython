"""
nombres=["bob","damian","tito","roberspier","bill"]
nomDup=[el*2 for el in nombres ]
print(nomDup)
"""
"""
#separador   
d1={("k1",88),("K2",2),("k3",78)}
d2={ key+"test" : value*5 for (key , value) in d1}
print(d2)
"""

#FFFFFFFFFFFFFFFFFFFFFFFFFf
"""
num=[3,6,8,10,15,23,50,44,8]
numDup=[el*2 for el in num if el%2==0 ]
print(numDup)

list1=[1,2,3,4,5,6]
list2=list1
print(list2[0])
list2[0]="hola"
print(list2[0])
print(list1)
list2=None
list2=list1[:]
print(list2)
list2[0]="sodio"
print(list1)

"""
"""
L1=[11,234,1,6435,22,78,1333,45,18,48]
L2=[ n for n in L1 if n>100 or n<20]
print(L2)
L3=[ n>100 for n in L1 ]
print(L3)
L4=all([ n>100 for n in L1 ])
print(L4)
"""

n='Faustino'
a=30
s=" vamo arriva {} solo son {} nomas ".format(n,a)

s2="{0} comio {1} tortas, y {0} calculo {1}*{1}".format(n,a)

fund=12312.4588
print('Funds:{}'.format(fund))
print('Funds:{:.1f}'.format(fund))
print('Funds:{:20.1f}'.format(fund))
print('Funds:{:<20.1f}'.format(fund))
print('Funds:{:>20.1f}'.format(fund))
print('Funds:{:^20.1f}'.format(fund))
print('Funds:{:-^20.1f}'.format(fund))

"""
m1='conan\''
print(m1)
m2='primero\nsegundo'
print(m2)
"""
"""

plata=20000
persona="Roberto"
mensaje=f'{persona} tiene en su cuenta {plata} dolares'
print(mensaje)
"""
"""

list_a=[2,4,7,8,9]
def function_mul(el):
    c= el*2
    return c

print(list(map(function_mul,list_a)))

list_a=[2,4,7,8,9]
print(list(map(lambda el:el*2,list_a)))
"""