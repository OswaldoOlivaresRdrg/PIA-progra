import requests
import os

def obtener_informacion_personaje(id_personaje):
    url = f"https://swapi.dev/api/people/{id_personaje}/"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_personaje = respuesta.json()
        return datos_personaje
    else:
        print("Error al obtener la información del personaje.")
        return None

def mostrar_caracteristicas_fisicas(datos_personaje):
    os.system('cls')
    print("Características Físicas de", datos_personaje['name'], ": ")
    print("Altura:", datos_personaje['height'])
    print("Peso:", datos_personaje['mass'])
    print("ojos: ", datos_personaje['eye_color'])
    print("Piel: ", datos_personaje['skin_color'])

def mostrar_datos_generales(datos_personaje):
    os.system('cls')
    print("Datos Generales de", datos_personaje['name'], ": ")
    print("Género:", datos_personaje['gender'])
    print("Año de nacimiento:", datos_personaje['birth_year'])
    nombre_planeta = obtener_nombres([datos_personaje['homeworld']])
    print("Lugar de nacimiento: ", nombre_planeta)
    lista_vechiculos = obtener_nombres(datos_personaje['vehicles'])
    print("Vehiculos: ", lista_vechiculos)
    nombres_naves = obtener_nombres(datos_personaje['starships'])
    print("Naves pilotadas:", nombres_naves)
    nombre_peliculas = obtener_nombres(datos_personaje['films'])
    print("Apariciones: ", nombre_peliculas)

def obtener_nombres(urls):
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            nombres.append(datos.get('name') or datos.get('title'))
    return nombres