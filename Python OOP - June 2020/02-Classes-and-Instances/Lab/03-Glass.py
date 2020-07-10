class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if ml > Glass.capacity:
            return f'Cannot add {ml} ml'
        self.content += ml
        Glass.capacity -= ml
        return f'Glass filled with {ml} ml'

    def empty(self):
        Glass.capacity += self.content
        self.content = 0
        return f'Glass is now empty'

    def info(self):
        return f'{Glass.capacity} ml left'