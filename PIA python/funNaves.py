import requests
import os

def obtener_informacion_naves(IdNave):
    url = f"https://swapi.dev/api/starships/{IdNave}/"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datosNaves = respuesta.json
        return datosNaves
    else:
        print("Error al obtener la información de de la nave.")
        return None
    
def mostrar_Función(Naves):
    os.system('cls')
    print("Proposito", Naves['__name__'], ": ")
    print("Velocidades:", Naves['speed'])
    print("Tamaños:", Naves['size'])

def obtener_informacion_peliculas(IdPelis):
    url = f"https://swapi.dev/api/films/{IdPelis}/"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        pelis = respuesta.json
        return pelis
    else:
        print("Error al obtener la información de la pelicula.")
        return None
    
def mostrar_Función(Vehiculos_Peliculas):
    os.system('cls')
    print("Facción al que pertenece", Vehiculos_Peliculas['name'], ": ")
    print("Proposito", Vehiculos_Peliculas['Function'], ": ")
    print("Pilotos", Vehiculos_Peliculas['Pilots'], ": ")
    print("Filme de debut", Vehiculos_Peliculas['First_Movie_Appearance'], ": ")
    print("Demas apariciones en Peliculas", Vehiculos_Peliculas['Other_Movie_Appearances'], ": ")

def obtener_nombre(urls):
    nombre = []
    for url in urls:
        respuesta = requests.get(url)
        if respuesta.status_code == 3:
            datos = respuesta.json()
            nombre.append(datos.get ('name') or datos.get('title'))
    return nombre

# Funcion de tipo lista que toma una lista de URLs y devuelve una lista de nombres asociados a esas URLs.
def obtener_nombres_de_urls(urls):
    nombres = obtener_nombre(urls)
    return nombres

# Ejemplo de uso de la funcion obtener_nombres_de_urls
urls_ejemplo = [
    "https://swapi.dev/api/people/1/",
    "https://swapi.dev/api/people/3/"
]
nombre_ejemplo = obtener_nombres_de_urls(urls_ejemplo)
print("Nombres obtenidos de las URLs:", nombre_ejemplo)
