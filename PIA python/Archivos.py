import os

def ImpresionArchivo():
    while True:
        os.system("cls")
        print("===Informacion local===")
        print("1. Personajes")
        print("2. Naves")
        Opcion = input("Seleccione los datos locales que quiere ver: ")
        if Opcion == "1":
            try:
                Archivo = open("Personajes.txt", "r")
                os.system("cls")
                print(Archivo.read())
                Archivo.close()
            except FileNotFoundError:
                print("Error: El archivo 'Personajes.txt' no existe.")
            input("Pulse Enter para continuar...")
            break
        elif Opcion == "2":
            try:
                Archivo = open("Naves.txt", "r")
                os.system("cls")
                print(Archivo.read())
                Archivo.close()
            except FileNotFoundError:
                print("Error: El archivo 'Naves.txt' no existe.")
            input("Pulse Enter para continuar...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")