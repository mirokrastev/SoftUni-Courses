class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.end < self.start:
            raise StopIteration
        i = self.start
        self.start += 1
        return i