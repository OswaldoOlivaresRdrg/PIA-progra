import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

#obtener datos de la API de Star Wars
def fetch_star_wars_data():
    url = "https://swapi.dev/api/people/"
    people = []

    while url:
        response = requests.get(url)
        data = response.json()
        people.extend(data['results'])
        url = data['next']

    return people

#guardar los datos en un archivo JSON
def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

#cargar los datos desde un archivo JSON
def load_data_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

#convertir los datos en un DataFrame de pandas
def data_to_dataframe(data):
    df = pd.DataFrame(data)
    return df

#generar gráficos
def generate_graphs(df):
    # Gráfica 1: Distribución de la altura de los personajes
    plt.figure(figsize=(10, 6))
    sns.histplot(df['height'].astype(float), bins=20, kde=True)
    plt.title('Distribución de la Altura de los Personajes de Star Wars')
    plt.xlabel('Altura (cm)')
    plt.ylabel('Frecuencia')
    plt.show()

    # Gráfica 2: Conteo de personajes por género
    plt.figure(figsize=(10, 6))
    sns.countplot(x='gender', data=df)
    plt.title('Conteo de Personajes por Género')
    plt.xlabel('Género')
    plt.ylabel('Conteo')
    plt.show()

    # Gráfica 3: Relación entre altura y masa
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='height', y='mass', data=df.astype({'height': 'float', 'mass': 'float'}))
    plt.title('Relación entre Altura y Masa de los Personajes de Star Wars')
    plt.xlabel('Altura (cm)')
    plt.ylabel('Masa (kg)')
    plt.show()

def main():
    # Obtener datos de la API
    data = fetch_star_wars_data()

    # Guardar datos en un archivo
    save_data_to_file(data, 'star_wars_data.json')

    # Cargar datos desde el archivo
    loaded_data = load_data_from_file('star_wars_data.json')

    # Convertir los datos en un DataFrame de pandas
    df = data_to_dataframe(loaded_data)

    # Filtrar las filas con datos no numéricos
    df = df[(df['height'].str.isnumeric()) & (df['mass'].str.isnumeric())]

    # Generar graf
    generate_graphs(df)

