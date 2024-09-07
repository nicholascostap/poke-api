import requests
import handler

URL = 'https://pokeapi.co/api/v2/'

class Pokemon:
    def __init__(self):
        self.name: str
        self.id: int
        self.experience: int
        self.ability: list[str]
        self.height: int
        self.weight: int
        self.types: list[str]
        self.moves: list[str]
        self.berries: list[str]
        self.evolutions: list[str]

    def get_pokemon(self):
        response = requests.get(f'{URL}pokemon/{self.name}')
        data = response.json()
        is_valid = handler.is_valid_response(response.status_code)
        if is_valid:
            self.set_pokemon(data)
        
    def set_pokemon(self, data: dict):
        self.name = data.get('name')
        self.id = data.get('id', 0)
        self.experience = data.get('base_experience', 0)
        self.ability = [skill.get('name') for skill in data.get('abilities')]
        self.height = data.get('height', 0)
        self.weight = data.get('weight')
        self.types = [typ.get('name') for typ in data.get('types')]
        self.moves = [move.get('move') for move in data.get('moves')]

    def get_evolution(self):
        response = requests.get(f'{URL}evolution-chain/{self.id}')
        data = response.json()
        is_valid = handler.is_valid_response(response.status_code)
        if is_valid:
            self.set_evolution(data)

    def set_evolution(self, data: dict):
        self.evolution = [evolution.get('name') for evolution in data.get('evolves_to')]

    def __str__(self):
        return f"""
        Name: {self.name}
        ID: {self.id}
        Experience: {self.experience}
        Ability: {self.ability}
        Height: {self.height}
        Weight: {self.weight}
        Types: {'\n'.join(self.types)}
        Moves: {'\n'.join(self.moves)}
        Evolutions: {'\n'.join(self.evolutions)}"""

if __name__ == '__main__':
    pokemon = Pokemon()
    pokemon.name = 'pikachu'
    pokemon.get_pokemon()
    print(pokemon)
    pokemon.get_evolution()
    print(pokemon)