lado=int(input("Entre el lado del cuadrado:"))
for i in range(lado):
    print("|")
    for i in range(lado):
        print("-", end="|")
    