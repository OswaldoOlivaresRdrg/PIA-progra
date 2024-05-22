import requests
import pandas as pd
#URL
base_url = "https://swapi.dev/"

response = requests.get(base_url + "people/") # Consulta ls información de personajes:
data = response.json()

characters = data['results'] # Extrae los datos 
df = pd.DataFrame(characters)

print(df.head()) # Mostrar registros para verificar
