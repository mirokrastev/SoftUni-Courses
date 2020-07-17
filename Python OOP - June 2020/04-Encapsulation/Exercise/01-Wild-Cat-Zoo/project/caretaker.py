from project.keeper import Keeper


class Caretaker(Keeper):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)