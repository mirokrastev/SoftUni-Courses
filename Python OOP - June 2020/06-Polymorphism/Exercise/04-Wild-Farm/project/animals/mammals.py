from project.animals.animal import Mammal


class Mouse(Mammal):
    FOOD = {'Vegetable', 'Fruit'}

    def make_sound(self):
        return 'Squeak'

    def feed(self, food):
        type_food = food.__class__.__name__
        if type_food not in Mouse.FOOD:
            return f'{self.__class__.__name__} does not eat {type_food}!'

        self.weight += food.quantity * 0.10
        self.food_eaten += food.quantity


class Dog(Mammal):
    FOOD = {'Meat'}

    def make_sound(self):
        return 'Woof!'

    def feed(self, food):
        type_food = food.__class__.__name__
        if type_food not in Dog.FOOD:
            return f'{self.__class__.__name__} does not eat {type_food}!'

        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity


class Cat(Mammal):
    FOOD = {'Vegetable', 'Meat'}

    def make_sound(self):
        return 'Meow'

    def feed(self, food):
        type_food = food.__class__.__name__
        if type_food not in Cat.FOOD:
            return f'{self.__class__.__name__} does not eat {type_food}!'

        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity


class Tiger(Mammal):
    FOOD = {'Meat'}

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food):
        type_food = food.__class__.__name__
        if type_food not in Tiger.FOOD:
            return f'{self.__class__.__name__} does not eat {type_food}!'

        self.weight += food.quantity * 1.00
        self.food_eaten += food.quantity