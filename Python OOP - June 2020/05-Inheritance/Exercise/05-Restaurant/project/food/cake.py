from project.food.dessert import Dessert


class Cake(Dessert):
    CAKE_PRICE = 5
    CAKE_GRAMS = 250
    CAKE_CALORIES = 1000

    def __init__(self, name):
        super().__init__(name, Cake.CAKE_PRICE, Cake.CAKE_GRAMS, Cake.CAKE_CALORIES)