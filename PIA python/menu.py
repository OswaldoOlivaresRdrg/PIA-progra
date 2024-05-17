import archivos
import subMenu
import os

def Opcion_1():
    while True:
        os.system('cls')
        print("Has seleccionado Consulta web.")
        print("1. personajes")
        print("2. Naves")
        print("3. Salir")
        Opcion = input("seleccione una opcion:")
        if Opcion == "1":
            subMenu.seleccion_especifica_personajes()
        elif Opcion == "2":
            subMenu.seleccion_especifica_naves()
        elif Opcion == "3":
            print("Regresando a menu principal...")
        else:
            os.system('cls')
            print("Opcion no valida")

def Opcion_2():
    while True:
        os.system('cls')
        print("Has seleccionado Consulta local.")
        print("1. personajes")
        print("2. Naves")
        print("3. Salir")
        Opcion = input("seleccione una opcion:")
        if Opcion == "1":
            subMenu.seleccion_especifica_personajes()
        elif Opcion == "2":
            subMenu.seleccion_especifica_naves()
        elif Opcion == "3":
            print("Regresando a menu principal...")
        else:
            os.system('cls')
            print("Opcion no valida")

def Opcion_3():
    print("Has seleccionado Animales.")

def Opcion_4():
    print("Has seleccionado Archivos.")
    print(archivos.Archivo.read())

def Opcion_salir():
    print("Saliendo del programa...")
    quit()