from random import randint


class RandomList(list):
    def get_random_element(self):
        index = randint(0, len(self) - 1)
        return self.pop(index)