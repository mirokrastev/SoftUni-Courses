class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        if money >= self.price and not self.owner:
            self.owner = owner
            return f'Successfully bought a {self.type}. Change: {money - self.price:.2f}'
        elif money < self.price:
            return 'Sorry, not enough money'
        elif self.owner:
            return 'Car already sold'

    def sell(self):
        if self.owner:
            self.owner = None
        elif not self.owner:
            return 'Vehicle has no owner'

    def __repr__(self):
        if self.owner:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        elif not self.owner:
            return f'{self.model} {self.type} is on sale: {self.price}'