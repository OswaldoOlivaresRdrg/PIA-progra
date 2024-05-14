import os
import funPersonajes
def seleccion_especifica_personajes():
    while True:
        os.system("cls")
        print("1. Caracteristicas Fisicas")
        print("2. Datos generales")
        print("3. Salir")
        SelectorSubmenu = input("selecciona lo que desees: ")
        if SelectorSubmenu == "1":
            DatosPersonaje = obtener_informacion_por_id()
            funPersonajes.mostrar_caracteristicas_fisicas(DatosPersonaje)
            input("Pulsa enter para continuar... ")
        elif SelectorSubmenu == "2":
            DatosPersonaje = obtener_informacion_por_id()
            funPersonajes.mostrar_datos_generales(DatosPersonaje)
            input("Pulsa enter para continuar... ")
        elif SelectorSubmenu == "3":
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
        selectorSubmenu = input("selecciona lo que desees: ")
        if selectorSubmenu == "1":
            print("Opcion en desarrollo")
            input("Pulsa enter para continuar... ")
        elif selectorSubmenu == "2":
            print("Opcion en desarrollo")
            input("Pulsa enter para continuar... ")
        elif selectorSubmenu == "3":
            print("Opcion en desarrollo")
            input("Pulsa enter para continuar... ")
        elif selectorSubmenu == "4":
            print("Regresando al inicio...")
            input("Pulsa enter para continuar... ")
            break

def obtener_informacion_por_id():
    while True:
        IdPersonaje = input("Ingrese el ID del personaje: ")
        try: 
            IdPersonaje = int(IdPersonaje)
            if IdPersonaje > 83:
                raise ValueError("Id no valida")
            DatosPersonaje = funPersonajes.obtener_informacion_personaje(IdPersonaje)
            return DatosPersonaje
            break
        except ValueError:
            print("Valor no válido")


