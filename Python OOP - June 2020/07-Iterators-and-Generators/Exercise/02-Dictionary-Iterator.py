class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_obj = dict_obj
        self.keys = list(self.dict_obj.keys())
        self.inx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.inx >= len(self.keys):
            raise StopIteration
        i = self.inx
        self.inx += 1
        return (self.keys[i], self.dict_obj[self.keys[i]])