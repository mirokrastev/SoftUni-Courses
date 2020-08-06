class vowels:
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        i = self.index
        self.index += 1

        if self.string[i].lower() in vowels.VOWELS:
            return self.string[i]
        return self.__next__()