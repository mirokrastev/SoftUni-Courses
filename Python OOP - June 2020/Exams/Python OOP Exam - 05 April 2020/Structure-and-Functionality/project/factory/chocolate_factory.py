from project.factory.factory import Factory


class ChocolateFactory(Factory):
    INGREDIENTS = {'white chocolate', 'dark chocolate', 'milk chocolate', 'sugar'}

    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_recipe(self, recipe_name, recipe: dict):
        if recipe_name not in self.recipes:
            self.recipes[recipe_name] = {}
        self.recipes[recipe_name].update(recipe)

    def make_chocolate(self, recipe_name):
        if recipe_name not in self.recipes:
            raise TypeError('No such recipe')

        if recipe_name not in self.products:
            self.products[recipe_name] = 0
        self.products[recipe_name] += 1

        for ingredient, quantity in self.recipes[recipe_name].items():
            try:
                self.ingredients[ingredient] -= quantity
                self.capacity += quantity
            except KeyError: continue