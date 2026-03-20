import requests
import json
import webbrowser

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_info(pokemon_name):
    url = BASE_URL + pokemon_name.lower()
    response = requests.get(url)

    try:
        pokemon_data = json.loads(response.text)
        pokemon_image = webbrowser.open(pokemon_data['sprites']['front_default'])
        print(f"Nombre: {pokemon_data['name']}")
        print(f"sprites: {pokemon_image}")
        print(f"Altura: {pokemon_data['height']}") 
        print(f"Peso: {pokemon_data['weight']}")
    except:
        print("No se encontro el pokemon")

if __name__ == "__main__":
    search_pokemom_name = input("Ingrese el nombre del pokemon: ")
    get_pokemon_info(search_pokemom_name)