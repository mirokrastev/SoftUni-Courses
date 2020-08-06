class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.high = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.high < 0:
            raise StopIteration
        i = self.high
        self.high -= 1
        return self.iterable[i]