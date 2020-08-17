from project.factory.factory import Factory


class PaintFactory(Factory):
    INGREDIENTS = {'white', 'yellow', 'blue', 'green', 'red'}

    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    @property
    def products(self):
        return self.ingredients