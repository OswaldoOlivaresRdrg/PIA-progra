import archivos
import subMenu
import graficas
import os

def Opcion_1():
    while True:
        os.system("cls")
        print("Has seleccionado consulta web.")
        print("1. Personajes")
        print("2. Naves")
        print("3. Salir")
        Opcion = input("Seleccione opcion: ")
        if Opcion == "1":
            subMenu.seleccion_especifica_personajes()
        elif Opcion == "2":
            subMenu.seleccion_especifica_naves()
        elif Opcion == "3":
            input("Pulsa enter para continuar... ")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def Opcion_2():
    print("Has seleccionado Consulta local.")
    Opcion_Archivos()

def Opcion_3():
    print("Has seleccionado Graficas.")
    graficas.main()

def Opcion_Archivos():
    archivos.ImpresionArchivo()

def Opcion_salir():
    subMenu.borrar_contenido()
    print("Saliendo del programa...")
    quit()
