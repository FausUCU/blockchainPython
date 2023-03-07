def pruebaLoop1():
    simbolo = "1"

    while True:
        if simbolo=="1":
            print("took")
            simbolo = input("ingrese el simbolo: ")
        elif simbolo=="2":
            print("chaca")
            simbolo = input("ingrese el simbolo: ")
        elif simbolo=="3":
            print("llllll")
            simbolo = input("ingrese el simbolo: ")
        elif simbolo=="4":
            simbolo="3"
            continue #igonara lo que sigue y comiensa de nuevo el loop
        elif simbolo=="5":
            break
    return None #devuelve nada
