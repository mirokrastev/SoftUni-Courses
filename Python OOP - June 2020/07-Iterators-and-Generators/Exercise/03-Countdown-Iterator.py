class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        current = self.count
        if current < 0:
            raise StopIteration
        self.count -= 1
        return current