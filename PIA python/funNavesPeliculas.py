import requests
import os

def obtener_informacion_naves(IdNave):
    url = f"https://swapi.dev/api/starships/{IdNave}/"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_naves = respuesta.json
        return datos_naves
    else:
        print("Error al obtener la información de de la nave.")
        return None

def obtener_informacion_peliculas(IdPelis):
    url = f"https://swapi.dev/api/films/{IdPelis}/"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        pelis = respuesta.json
        return pelis
    else:
        print("Error al obtener la información de la pelicula.")
        return None