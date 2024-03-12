import requests
from ascii_magic import AsciiArt

class Pokemon:
    def __init__(self, poke_id, name, height, weight, image_url):
        self.id = poke_id
        self.name = name
        self.height = height
        self.weight = weight
        self.image_url = image_url

    def __repr__(self):
        return f"(pokemon name: {self.name} | id: {self.id})"
    
    def __str__(self):
        art = AsciiArt.from_url(self.image_url)
        art_string = art.to_ascii()
        return f"{art_string}\nName:{self.name}\nHeight: {self.height}\nWeight: {self.weight}"


class PokeAPI:
    base_url = "https://pokeapi.co/api/v2/"


    def __get(self, endpoint, id_or_name):
        request_url = self.base_url + endpoint + '/' + id_or_name
        response = requests.get(request_url)
        if response.ok:
            return response.json()
        else:
            return None
        

    def get_pokemon(self, poke_name):
        data = self.__get('pokemon', poke_name.lower())
        if data:
            poke_id = data.get('id')
            name = data.get('name')
            height = data.get('height')
            weight = data.get('weight')
            image_url = data.get('sprites').get('back_shiny')
            new_pokemon = Pokemon(poke_id, name, height, weight, image_url)
            return new_pokemon
        else:
            print("There is no such pokemon")

client = PokeAPI()

while True:
    pokemon = input('Choose your pokemon: ')
    if pokemon == 'Quit':
        break
    pokemon = client.get_pokemon(pokemon)
    print(pokemon)
