class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        self.quantity += milliliters
        self.quantity = min(self.quantity, self.size)

    def status(self):
        return self.size - self.quantity