class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int):
        if Glass.capacity <= self.content + ml:
            return f'Cannot add {ml} ml'

        self.content += ml
        return f'Glass filled with {ml} ml'

    def empty(self):
        self.content = 0
        return f'Glass is now empty'

    def info(self):
        left_space = Glass.capacity - self.content
        return f'{left_space} ml left'