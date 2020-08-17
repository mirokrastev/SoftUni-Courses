from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name, chocolate_factory: ChocolateFactory, egg_factory: EggFactory,
                 paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}

    def add_chocolate_ingredient(self, type, quantity):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type, quantity):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type, quantity):
        self.paint_factory.add_ingredient(type, quantity)

    def paint_egg(self, color, egg_type):
        if color not in self.paint_factory.ingredients \
                or egg_type not in self.egg_factory.ingredients:
            raise ValueError('Invalid commands')
        self.paint_factory.remove_ingredient(color, 1)
        self.egg_factory.remove_ingredient(egg_type, 1)

        colored_egg = f'{color} {egg_type}'
        if colored_egg not in self.storage:
            self.storage[colored_egg] = 0
        self.storage[colored_egg] += 1

    def make_chocolate(self, recipe):
        self.chocolate_factory.make_chocolate(recipe)
        if recipe not in self.storage:
            self.storage[recipe] = 0
        self.storage[recipe] += 1

    def __repr__(self):
        storage_items = "\n".join(f'{key}: {value}' for key, value in self.storage.items())
        return f'Shop name: {self.name}\nShop Storage:\n{storage_items}'