class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def is_not_ordered(self):
        return True if not self.ordered else False

    def add_extra(self, ingredient, quantity, ingredient_price):
        if self.is_not_ordered():
            if ingredient not in self.ingredients:
                self.ingredients[ingredient] = 0
            self.ingredients[ingredient] += quantity
            self.price += quantity * ingredient_price
        else:
            return f'Pizza {self.name} already prepared and we can\'t make any changes!'

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if self.is_not_ordered():
            if ingredient not in self.ingredients:
                return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'

            if self.ingredients[ingredient] < quantity:
                return f'Please check again the desired quantity of {ingredient}!'

            self.ingredients[ingredient] -= quantity
            self.price -= quantity * ingredient_price
        else:
            return f'Pizza {self.name} already prepared and we can\'t make any changes!'

    def pizza_ordered(self):
        self.ordered = True
        ingredients = [f'{k}: {v}' for k, v in self.ingredients.items()]
        return f'You\'ve ordered pizza {self.name} prepared with {", ".join(ingredients)} ' \
               f'and the price will be {self.price}lv.'