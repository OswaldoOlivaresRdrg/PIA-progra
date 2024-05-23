import os
import funPersonajes
import funNavesPeliculas
import archivos

def seleccion_especifica_personajes():
    while True:
        os.system("cls")
        print("1. Caracteristicas Fisicas")
        print("2. Datos generales(guardar de forma local)")
        print("3. Salir")
        SelectorSubMenu = input("selecciona lo que desees: ")
        if SelectorSubMenu == "1":
            DatosPersonaje = obtener_informacion_id_personaje()
            funPersonajes.mostrar_caracteristicas_fisicas(DatosPersonaje)
            input("Pulsa enter para continuar... ")
        elif SelectorSubMenu == "2":
            DatosPersonaje = obtener_informacion_id_personaje()
            funPersonajes.mostrar_datos_generales(DatosPersonaje)
            input("Pulsa enter para continuar... ")
        elif SelectorSubMenu == "3":
            print("Regresando al inicio...")
            input("Pulsa enter para continuar... ")
            break

def seleccion_especifica_naves():
    while True:
        os.system("cls")
        print("1. Datos importantes")
        print("2. Datos detallados(guardar de forma local)")
        print("3. Salir")
        SelectorSubMenu = input("selecciona lo que desees: ")
        if SelectorSubMenu == "1":
            print("Opcion en desarrollo")
            DatosNave = obtener_informacion_id_naves()
            funNavesPeliculas.propiedades_naves(DatosNave)
            input("Pulsa enter para continuar... ")
        elif SelectorSubMenu == "2":
            print("Opcion en desarrollo")
            DatosNave = obtener_informacion_id_naves()
            funNavesPeliculas.informacion_detallada(DatosNave)
            input("Pulsa enter para continuar... ")
        elif SelectorSubMenu == "3":
            print("Regresando al inicio...")
            input("Pulsa enter para continuar... ")
            break

def obtener_informacion_id_personaje():
    while True:
        idPersonaje = input("Ingrese el ID del personaje: ")
        try: 
            idPersonaje = int(idPersonaje)
            if idPersonaje > 83:
                raise ValueError("Id no valida")
            DatosPersonaje = funPersonajes.obtener_informacion_personaje(idPersonaje)
            return DatosPersonaje
            break
        except ValueError:
            print("Valor no válido")

def obtener_informacion_id_naves():
    while True:
        idNave = input("Ingrese el ID de la nave: ")
        try:
            idNave = int(idNave)
            DatosNave = funNavesPeliculas.obtener_informacion_naves(idNave)
            if DatosNave is not None:
                return DatosNave
            else:
                print("Error al obtener la información de la nave.")
        except ValueError:
            print("Valor no válido. Por favor, ingrese un número entero.")\
            
def borrar_contenido():
    while True:
        print("¿Desea borrar los datos de búsqueda?")
        print("1. Sí")
        print("2. No")
        Opcion = input("Seleccione opción: ")
        
        if Opcion == '1':  # '1' debe ser una cadena, no un entero
            archivos = ['Personajes.txt', 'Naves.txt']
            for nombre_archivo in archivos:
                try:
                    with open(nombre_archivo, 'w') as archivo:
                        archivo.write('')
                    print(f"El contenido de {nombre_archivo} ha sido borrado.")
                except FileNotFoundError:
                    print(f"Error: El archivo {nombre_archivo} no existe.")
            break
        elif Opcion == '2':
            print("Se conservarán los datos.")
            break 
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

