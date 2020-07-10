from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return f'This pokemon is already caught'

        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name):
        pokemon_var = [i.name for i in self.pokemon]
        if pokemon_name not in pokemon_var:
            return f'Pokemon is not caught'

        inx = pokemon_var.index(pokemon_name)
        self.pokemon.pop(inx)
        return f'You have released {pokemon_name}'

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\n' \
                 f'Pokemon count {len(self.pokemon)}\n'

        for i in self.pokemon:
            result += f'- {i.pokemon_details()}\n'

        return result