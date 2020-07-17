class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size // 2)

    def add_item(self, item_name):
        if len(self.items.values()) >= self.capacity:
            return f'Not enought capacity in the store'

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f'{item_name} added to the store'

    def remove_item(self, item_name, amount):
        if item_name not in self.items:
            return f'Cannot remove {amount} {item_name}'

        if amount > self.items[item_name]:
            return f'Cannot remove {amount} {item_name}'

        self.items[item_name] -= amount
        return f'{amount} {item_name} removed from the store'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'