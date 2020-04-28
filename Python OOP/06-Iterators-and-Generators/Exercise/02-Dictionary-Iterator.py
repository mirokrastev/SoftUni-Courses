class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_obj = dict_obj
        self.key = list(self.dict_obj.keys())
        self.index = 0
        self.dict_length = len(self.key)

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index

        if index == self.dict_length:
            raise StopIteration

        key = self.key[index]
        value = self.dict_obj[key]
        self.index += 1

        return (current_key, current_value)