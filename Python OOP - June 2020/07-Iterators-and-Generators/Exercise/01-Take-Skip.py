class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number >= self.step * self.count:
            raise StopIteration
        i = self.number
        self.number += self.step
        return i