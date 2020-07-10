class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        needed_fuel = kilometers * self.fuel_consumption
        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel


class Motorcycle(Vehicle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


class RaceMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
    DEFAULT_FUEL_CONSUMPTION = 8


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


class Car(Vehicle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
    DEFAULT_FUEL_CONSUMPTION = 3


class FamilyCar(Car):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

class SportCar(Car):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
    DEFAULT_FUEL_CONSUMPTION = 10