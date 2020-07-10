class Lion:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Lion'

    def get_needs(self):
        return 50

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Tiger:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Tiger'

    def get_needs(self):
        return 45

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Cheetah:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Cheetah'

    def get_needs(self):
        return 60

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


class Keeper:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = 'Keeper'

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Caretaker:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = 'Caretaker'

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Vet:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = 'Vet'

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if price > self.__budget:
                return 'Not enough budget'
        else:
            return f'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.type} added to the zoo'

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.type} hired successfully'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        to_pay = sum([i.salary for i in self.workers])
        if to_pay > self.__budget:
            return f'You have no budget to pay your workers. They are unhappy'

        self.__budget -= to_pay
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        to_pay = sum([i.get_needs() for i in self.animals])
        if to_pay > self.__budget:
            return 'You have no budget to tend the animals. They are unhappy.'

        self.__budget -= to_pay
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        for animal_type in ('Lion', 'Tiger', 'Cheetah'):
            result += f'----- {len([animal for animal in self.animals if animal.type == animal_type])} {animal_type}s:\n'
            for animal_var in [animal for animal in self.animals if animal.type == animal_type]:
                result += f'{repr(animal_var)}\n'

        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        for worker_type in ('Keeper', 'Caretaker', 'Vet'):
            result += f'----- {len([worker for worker in self.workers if worker.type == worker_type])} {worker_type}s:\n'
            for worker_var in [worker for worker in self.workers if worker.type == worker_type]:
                result += f'{repr(worker_var)}\n'

        return result