import requests
import os

def obtener_informacion_personaje(id_personaje):
    url = f"https://swapi.dev/api/people/{id_personaje}/"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        DatosPersonaje = respuesta.json()
        return DatosPersonaje
    else:
        print("Error al obtener la información del personaje.")
        return None

def mostrar_caracteristicas_fisicas(DatosPersonaje):
    os.system('cls')
    print("Características Físicas de", DatosPersonaje['name'], ": ")
    print("Altura:", DatosPersonaje['height'])
    print("Peso:", DatosPersonaje['mass'])
    print("ojos: ", DatosPersonaje['eye_color'])
    print("Piel: ", DatosPersonaje['skin_color'])
    with open("PIA.txt", "a") as f:
        f.write("Características Físicas de"+ DatosPersonaje['name']+ ": \n")
        f.write("Altura:"+ DatosPersonaje['height']+ ": \n")
        f.write("Peso:"+ DatosPersonaje['mass']+ " \n")
        f.write("ojos: "+ DatosPersonaje['eye_color']+ " \n")
        f.write("Piel: "+ DatosPersonaje['skin_color']+ "\n")
        print("se guardo correctamente")
        


def mostrar_datos_generales(DatosPersonaje):
    os.system('cls')
    print("Datos Generales de", DatosPersonaje['name'], ": ")
    print("Género:", DatosPersonaje['gender'])
    print("Año de nacimiento:", DatosPersonaje['birth_year'])
    nombrePlaneta = obtener_nombres([DatosPersonaje['homeworld']])
    print("Lugar de nacimiento: ", nombrePlaneta)
    listaVehiculos = obtener_nombres(DatosPersonaje['vehicles'])
    print("Vehiculos: ", listaVehiculos)
    nombreNaves = obtener_nombres(DatosPersonaje['starships'])
    print("Naves pilotadas:", nombreNaves)
    nombrePeliculas = obtener_nombres(DatosPersonaje['films'])
    print("Apariciones: ", nombrePeliculas)
    with open("PIA.txt", "a") as f:
        f.write("Datos Generales de"+ DatosPersonaje['name']+ ": \n")
        f.write("Género:"+ DatosPersonaje['gender']+ ": \n")
        f.write("Año de nacimiento:"+ DatosPersonaje['birth_year']+ " \n")
        f.write("Lugar de nacimiento: "+ str(nombrePlaneta)+ " \n")
        f.write("Vehiculos: "+ str(listaVehiculos)+ "\n")
        f.write("Naves pilotadas:"+ str(nombreNaves)+ "\n")
        f.write("Apariciones: "+ str(nombrePeliculas)+ "\n")
        print("se guardo correctamente")

def obtener_nombres(urls):
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            nombres.append(datos.get('name') or datos.get('title'))
    return nombres