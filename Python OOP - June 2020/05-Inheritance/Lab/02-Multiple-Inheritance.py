class Person:
    def sleep(self):
        return 'sleeping...'


class Employee():
    def get_fired(self):
        return 'fired...'


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'