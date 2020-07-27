from typing import List


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def return_name(self):
        return f'{self.name} {self.surname}'

    def __add__(self, obj):
        return Person(self.name, obj.surname)


class Group:
    def __init__(self, name, people: List[Person]):
        self.name = name
        self.people = people

    def __add__(self, obj):
        return Group(self.name + obj.name, self.people + obj.people)

    def __len__(self):
        return len(self.people)

    def __getitem__(self, index):
        name = self.people[index].return_name()
        return f'Person {index}: {name}'

    def __str__(self):
        return f'Group {self.name} with members {", ".join(person.return_name() for person in self.people)}'