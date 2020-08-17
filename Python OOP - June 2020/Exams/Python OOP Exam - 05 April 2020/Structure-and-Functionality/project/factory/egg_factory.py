from project.factory.factory import Factory


class EggFactory(Factory):
    INGREDIENTS = {'chicken egg', 'quail egg'}

    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    @property
    def products(self):
        return self.ingredients