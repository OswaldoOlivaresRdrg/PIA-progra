import os
import FunPersonajes
def seleccion_especifica_personajes():
    while True:
        os.system("cls")
        print("1. Caracteristicas Fisicas")
        print("2. Datos generales")
        print("3. Salir")
        selectorSubMenu = input("selecciona lo que desees: ")
        if selectorSubMenu == "1":
            datosPersonaje = obtener_informacion_por_id()
            FunPersonajes.mostrar_caracteristicas_fisicas(datosPersonaje)
            input("Pulsa enter para continuar... ")
        elif selectorSubMenu == "2":
            datosPersonaje = obtener_informacion_por_id()
            FunPersonajes.mostrar_datos_generales(datosPersonaje)
            input("Pulsa enter para continuar... ")
        elif selectorSubMenu == "3":
            print("Regresando al inicio...")
            input("Pulsa enter para continuar... ")
            break

def seleccion_especifica_naves():
    while True:
        os.system("cls")
        print("1. Velocidad maxima")
        print("2. Distancia maxima")
        print("3. Poder de ataque")
        print("4. Salir")
        selectorSubMenu = input("selecciona lo que desees: ")
        if selectorSubMenu == "1":
            print("Opcion en desarrollo")
            input("Pulsa enter para continuar... ")
        elif selectorSubMenu == "2":
            print("Opcion en desarrollo")
            input("Pulsa enter para continuar... ")
        elif selectorSubMenu == "3":
            print("Opcion en desarrollo")
            input("Pulsa enter para continuar... ")
        elif selectorSubMenu == "4":
            print("Regresando al inicio...")
            input("Pulsa enter para continuar... ")
            break

def obtener_informacion_por_id():
    while True:
        idPersonaje = input("Ingrese el ID del personaje: ")
        try: 
            idPersonaje = int(idPersonaje)
            if idPersonaje > 83:
                raise ValueError("Id no valida")
            datosPersonaje = FunPersonajes.obtener_informacion_personaje(idPersonaje)
            return datosPersonaje
            break
        except ValueError:
            print("Valor no válido")


