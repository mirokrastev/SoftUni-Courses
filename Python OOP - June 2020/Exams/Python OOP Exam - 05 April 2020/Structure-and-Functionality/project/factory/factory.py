from abc import ABC, abstractmethod


class Factory(ABC):
    INGREDIENTS = {}

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    def add_ingredient(self, ingredient_type, quantity):
        if ingredient_type not in self.__class__.INGREDIENTS:
            raise TypeError(f'Ingredient of type {ingredient_type} '
                            f'not allowed in {self.__class__.__name__}')

        if not self.can_add(quantity):
            raise ValueError('Not enough space in factory')

        if ingredient_type not in self.ingredients:
            self.ingredients[ingredient_type] = 0
        self.ingredients[ingredient_type] += quantity
        self.capacity -= quantity

    def remove_ingredient(self, ingredient_type, quantity):
        if ingredient_type not in self.ingredients:
            raise KeyError('No such product in the factory')

        if quantity > self.ingredients[ingredient_type]:
            raise ValueError('Ingredient quantity cannot be less than zero')

        self.ingredients[ingredient_type] -= quantity
        self.capacity += quantity

    def can_add(self, value):
        return self.capacity >= value