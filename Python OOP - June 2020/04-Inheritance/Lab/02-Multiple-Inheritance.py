class Person:
    def sleep(self):
        return 'sleeping...'

class Employee():
    def get_fired(self):
        return 'fired...'

class Teacher(Employee, Person):
    def teach(self):
        return 'teaching...'