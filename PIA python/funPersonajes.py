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
    nombre_personaje = DatosPersonaje['name']
    informacion_nueva = (
        f"\nDatos Generales de {nombre_personaje}: \n"
        f"Altura: {DatosPersonaje['height']}: \n"
        f"Género: {DatosPersonaje['gender']}: \n"
        f"Peso: {DatosPersonaje['mass']} \n"
        f"Ojos: {DatosPersonaje['eye_color']} \n"
        f"Piel: {DatosPersonaje['skin_color']}\n"
        f"Año de nacimiento: {DatosPersonaje['birth_year']} \n"
        f"Lugar de nacimiento: {str(nombrePlaneta)} \n"
        f"Vehiculos: {str(listaVehiculos)}\n"
        f"Naves pilotadas: {str(nombreNaves)}\n"
        f"Apariciones: {str(nombrePeliculas)}\n"
        "\n"
    )

    try:
        with open("Personajes.txt", "r") as f:
            contenido_actual = f.read()
    except FileNotFoundError:
        contenido_actual = ""

    if informacion_nueva.strip() in contenido_actual:
        print("La información ya existe y no se agregará nuevamente.")
    else:
        with open("Personajes.txt", "a") as f:
            f.write(informacion_nueva)
        print("La información se guardó correctamente.")

def obtener_nombres(urls):
    nombres = []
    for url in urls:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            nombres.append(datos.get('name') or datos.get('title'))
    return nombres