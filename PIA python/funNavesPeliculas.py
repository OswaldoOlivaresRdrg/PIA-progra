import requests
import os

def obtener_informacion_naves(IdNave):
    url = f"https://swapi.dev/api/starships/{IdNave}/"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanzará una excepción si el código de estado indica un error

        DatosNaves = respuesta.json()  # Intenta obtener los datos en formato JSON
        
        # Verificar si la respuesta contiene "detail": "Not found"
        if DatosNaves.get("detail") == "Not found":
            print("La nave no fue encontrada en la API.")
            return None

        return DatosNaves

    except requests.exceptions.HTTPError as http_err:
        os.system("cls")
        print(f"Error HTTP al obtener la información de la nave: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        os.system("cls")
        print(f"Error de conexión al obtener la información de la nave: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        os.system("cls")
        print(f"Tiempo de espera agotado al obtener la información de la nave: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        os.system("cls")
        print(f"Error en la solicitud al obtener la información de la nave: {req_err}")
    except Exception as e:
        os.system("cls")
        print(f"Otro error ocurrió al obtener la información de la nave: {e}")

    return None

def obtener_informacion_peliculas(IdPelis):
    url = f"https://swapi.dev/api/films/{IdPelis}/"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        pelis = respuesta.json()
        return pelis
    else:
        print("Error al obtener la información de la pelicula.")
        return None

def propiedades_naves(DatosNaves):
    os.system("cls")
    print("Nave: ", DatosNaves['name'])
    print("Velocidad: ", DatosNaves['max_atmosphering_speed'])
    print("Tamaños:", DatosNaves['length'])
    print("Tipo de nave: ", DatosNaves['starship_class'])
    
def informacion_detallada(DatosNaves):
    os.system("cls")
    print("informacion de", DatosNaves['name'], ": ")
    print("Modelo de nave: ", DatosNaves['model'])
    print("Fabricado por: ", DatosNaves['manufacturer'])
    print("Costo: ", DatosNaves['cost_in_credits'])
    print("Grupo: ", DatosNaves['crew'])
    print("Pasajeros: ", DatosNaves['passengers'])
    print("Capacidad de carga: ", DatosNaves['cargo_capacity'])
    print("Hipervelocidad:", DatosNaves['hyperdrive_rating'])
    nombrePeliculas = obtener_nombres(DatosNaves['films'])
    print("Apariciones: ", nombrePeliculas)
    nombre_nave = DatosNaves['name']
    informacion_nueva = (
        f"\ninformacion de {nombre_nave}: \n"
        f"Modelo de nave: {DatosNaves['model']}: \n"
        f"Velocidad: {DatosNaves['max_atmosphering_speed']}: \n"
        f"Tamaños: {DatosNaves['length']} \n"
        f"Tipo de nave: {DatosNaves['starship_class']} \n"
        f"Fabricado por: {DatosNaves['manufacturer']} \n"
        f"Costo: {DatosNaves['cost_in_credits']} \n"
        f"Grupo: {DatosNaves['crew']} \n"
        f"Capacidad de carga: {DatosNaves['cargo_capacity']} \n"
        f"Hipervelocidad: {DatosNaves['hyperdrive_rating']} \n"
        "\n"
    )

    try:
        with open("Naves.txt", "r") as f:
            contenido_actual = f.read()
    except FileNotFoundError:
        contenido_actual = ""

    if informacion_nueva.strip() in contenido_actual:
        print("La información ya existe y no se agregará nuevamente.")
    else:
        with open("Naves.txt", "a") as f:
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