from project.animals.animal import Bird


class Owl(Bird):
    FOOD = {'Meat'}

    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food):
        type_food = food.__class__.__name__
        if type_food not in Owl.FOOD:
            return f'{self.__class__.__name__} does not eat {type_food}!'

        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):
    FOOD = {'Vegetable', 'Fruit', 'Meat', 'Seed'}

    def make_sound(self):
        return 'Cluck'

    def feed(self, food):
        type_food = food.__class__.__name__
        if type_food not in Hen.FOOD:
            return f'{self.__class__.__name__} does not eat {type_food}!'

        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity