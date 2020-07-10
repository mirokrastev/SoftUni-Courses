class custom_range:
    def __init__(self, start, end):
        self.i = start
        self.n = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.i:
            raise StopIteration
        i = self.i
        self.i += 1

        return i