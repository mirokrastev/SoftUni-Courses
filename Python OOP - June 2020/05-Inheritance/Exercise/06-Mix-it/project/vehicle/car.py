from project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats: int, fuel_tank: int, fuel_consumption: float, fuel: float):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value + self.__fuel <= self.fuel_tank:
            self.__fuel = value
        else:
            self.__fuel = self.fuel_tank

    def drive(self, distance):
        needed_fuel = distance * self.fuel_consumption
        if needed_fuel <= self.__fuel:
            self.__fuel -= needed_fuel
            return "We've enjoyed the travel!"

    def refuel(self, liters):
        total_fuel = self.__fuel + liters
        if self.get_capacity(self.fuel_tank, total_fuel) != 'Capacity reached!':
            self.__fuel += liters
        return self.__fuel
