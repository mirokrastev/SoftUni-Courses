from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self): pass

    @abstractmethod
    def feed(self, food): pass


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        class_animal = self.__class__.__name__
        return f'{class_animal} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        class_animal = self.__class__.__name__
        return f'{class_animal} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'