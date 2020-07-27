from project.product import Product


class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.grams = grams

    @property
    def grams(self):
        return self._grams

    @grams.setter
    def grams(self, grams):
        self._grams = grams