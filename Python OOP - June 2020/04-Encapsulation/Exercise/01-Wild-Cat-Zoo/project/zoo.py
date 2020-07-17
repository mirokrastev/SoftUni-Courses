from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price > self.__budget:
            return f'Not enough budget'

        if len(self.animals) >= self.__animal_capacity:
            return f'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return f'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        workers_var = [i.name for i in self.workers]

        if worker_name not in workers_var:
            return f'There is no {worker_name} in the zoo'

        inx = workers_var.index(worker_name)

        self.workers.pop(inx)
        return f'{worker_name} fired successfully'

    def pay_workers(self):
        summed_salaries = sum([i.salary for i in self.workers])

        if summed_salaries > self.__budget:
            return f'You have no budget to pay your workers. They are unhappy'

        self.__budget -= summed_salaries
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        summed_bill = sum([i.get_needs() for i in self.animals])

        if summed_bill > self.__budget:
            return f'You have no budget to tend the animals. They are unhappy.'

        self.__budget -= summed_bill
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        lions_info = '\n'.join([a.__repr__() for a in lions])
        tigers_info = '\n'.join([t.__repr__() for t in tigers])
        cheetahs_info = '\n'.join([c.__repr__() for c in cheetahs])

        return f'You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n{lions_info}\n' \
               f'----- {len(tigers)} Tigers:\n{tigers_info}\n----- {len(cheetahs)} Cheetahs:\n{cheetahs_info}'

    def workers_status(self):
        keepers = [person for person in self.workers if person.__class__.__name__ == 'Keeper']
        caretakers = [person for person in self.workers if person.__class__.__name__ == 'Caretaker']
        vets = [person for person in self.workers if person.__class__.__name__ == 'Vet']
        keepers_info = '\n'.join([keeper.__repr__() for keeper in keepers])
        caretakers_info = '\n'.join([caretaker.__repr__() for caretaker in caretakers])
        vets_info = '\n'.join([vet.__repr__() for vet in vets])

        return f'You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n{keepers_info}\n' \
               f'----- {len(caretakers)} Caretakers:\n{caretakers_info}\n----- {len(vets)} Vets:\n{vets_info}'