class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        return self.__data.pop()

    def peek(self):
        return self.__data[-1]

    def is_empty(self):
        return len(self.__data) == 0

    def __repr__(self):
        return f'{self.__data[::-1]}'