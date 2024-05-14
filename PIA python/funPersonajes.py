import requests
import os

def obtener_informacion_personaje(id_personaje):
    url = f"https://swapi.dev/api/people/{id_personaje}/"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datosPersonaje = respuesta.json()
        return datosPersonaje
    else:
        print("Error al obtener la información del personaje.")
        return None

def mostrar_caracteristicas_fisicas(datosPersonaje):
    os.system('cls')
    print("Características Físicas de", datosPersonaje['name'], ": ")
    print("Altura:", datosPersonaje['height'])
    print("Peso:", datosPersonaje['mass'])
    print("ojos: ", datosPersonaje['eye_color'])
    print("Piel: ", datosPersonaje['skin_color'])

def mostrar_datos_generales(datosPersonaje):
    os.system('cls')
    print("Datos Generales de", datosPersonaje['name'], ": ")
    print("Género:", datosPersonaje['gender'])
    print("Año de nacimiento:", datosPersonaje['birth_year'])
    nombrePlaneta = obtener_nombres([datosPersonaje['homeworld']])
    print("Lugar de nacimiento: ", nombrePlaneta)
    listaVehiculos = obtener_nombres(datosPersonaje['vehicles'])
    print("Vehiculos: ", listaVehiculos)
    nombreNaves = obtener_nombres(datosPersonaje['starships'])
    print("Naves pilotadas:", nombreNaves)
    nombrePeliculas = obtener_nombres(datosPersonaje['films'])
    print("Apariciones: ", nombrePeliculas)

def obtener_nombres(urls):
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            nombres.append(datos.get('name') or datos.get('title'))
    return nombres