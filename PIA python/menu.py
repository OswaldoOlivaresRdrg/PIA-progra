import archivos
import subMenu

def Opcion_1():
    print("Has seleccionado Personajes.")
    subMenu.seleccion_especifica_personajes()

def Opcion_2():
    print("Has seleccionado Naves.")
    subMenu.seleccion_especifica_naves()

def Opcion_3():
    print("Has seleccionado Animales.")

def Opcion_4():
    print("Has seleccionado Archivos.")
    print(archivos.Archivo.read())

def Opcion_salir():
    print("Saliendo del programa...")
    quit()
