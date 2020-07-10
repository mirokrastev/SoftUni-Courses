class CustomList:
    def __init__(self, *args):
        self.custom_list = [i for i in args]

    def append(self, value):
        self.custom_list.append(value)
        return self.custom_list

    def remove(self, index: int):
        return self.custom_list.pop(index)

    def get(self, index: int):
        return self.custom_list[index]

    def extend(self, iterable: iter):
        self.custom_list.extend(iterable)
        return self.custom_list

    def insert(self, index: int, value):
        self.custom_list.insert(index, value)
        return self.custom_list

    def pop(self):
        return self.custom_list.pop()

    def clear(self):
        self.custom_list.clear()

    def index(self, value):
        return self.custom_list.index(value)

    def count(self, value):
        return self.custom_list.count(value)

    def reverse(self):
        self.custom_list.reverse()
        return self.custom_list

    def copy(self):
        return self.custom_list.copy()

    def size(self):
        return len(self.custom_list)

    def add_first(self, value):
        self.custom_list.insert(0, value)

    def dictionalize(self):
        list_var = self.custom_list
        return {list_var[i]: list_var[i+1] for i in range(0, len(list_var), 2)}

    def move(self, amount: int):
        removed_amount = [self.custom_list.pop(0) for i in range(len(self.custom_list)) if i < amount]
        self.custom_list.extend(removed_amount)
        return self.custom_list

    def sum(self):
        return sum([i if isinstance(i, int) else len(i) for i in self.custom_list])

    def overbound(self):
        return self.custom_list.index(max(self.custom_list))

    def underbound(self):
        return self.custom_list.index(min(self.custom_list))