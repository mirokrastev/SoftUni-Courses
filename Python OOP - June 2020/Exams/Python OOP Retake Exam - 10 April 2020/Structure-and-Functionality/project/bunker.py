from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor
from typing import List


class Bunker:
    def __init__(self):
        self.survivors: List[Survivor] = []
        self.supplies: List[Supply] = []
        self.medicine: List[Medicine] = []

    @property
    def food(self):
        foods = [f for f in self.supplies if f.__class__.__name__ == 'FoodSupply']

        if not foods:
            raise IndexError('There are no food supplies left!')
        return foods

    @property
    def water(self):
        waters = [w for w in self.supplies if w.__class__.__name__ == 'WaterSupply']

        if not waters:
            raise IndexError('There are no water supplies left!')
        return waters

    @property
    def painkillers(self):
        painkillers = [p for p in self.medicine if p.__class__.__name__ == 'Painkiller']

        if not painkillers:
            raise IndexError('There are no painkillers left!')
        return painkillers

    @property
    def salves(self):
        salves = [s for s in self.medicine if s.__class__.__name__ == 'Salve']

        if not salves:
            raise IndexError('There are no salves left!')
        return salves

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type):
        if not survivor.needs_healing:
            return

        med = [med for med in self.medicine if med.__class__.__name__ == medicine_type]

        if not med: return
        med = med[-1]
        self.medicine.remove(med)
        med.apply(survivor)
        return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor: Survivor, sustenance_type):
        if not survivor.needs_sustenance:
            return

        sus = [sus for sus in self.supplies if sus.__class__.__name__ == sustenance_type]

        if not sus: return
        sus = sus[-1]
        self.supplies.remove(sus)
        sus.apply(survivor)
        return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

            water = [w for w in self.supplies if w.__class__.__name__ == 'WaterSupply'][0]
            self.supplies.remove(water)

            food = [f for f in self.supplies if f.__class__.__name__ == 'FoodSupply'][0]
            self.supplies.remove(food)

            water.apply(survivor)
            food.apply(survivor)