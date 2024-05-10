import archivos
import subMenu

def opcion_1():
    print("Has seleccionado Personajes.")
    subMenu.seleccion_especifica_personajes()

def opcion_2():
    print("Has seleccionado Naves.")
    subMenu.seleccion_especifica_naves()

def opcion_3():
    print("Has seleccionado Animales.")

def opcion_4():
    print("Has seleccionado Archivos.")
    print(archivos.Archivo.read())

def opcion_salir():
    print("Saliendo del programa...")
    quit()
