class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        var = self.iterable[self.index]
        self.index -= 1
        
        return var