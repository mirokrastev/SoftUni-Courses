class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.animals = []
        self.name = name

    def register_animal(self, animal_name):
        if len(Vet.animals) == Vet.space:
            return f'Not enough space'

        Vet.animals.append(animal_name)
        self.animals.append(animal_name)

        return f'{animal_name} registered in the clinic'

    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f'{animal_name} not in the clinic'

        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)

        return f'{animal_name} unregistered successfully'

    def info(self):
        return f'{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic'