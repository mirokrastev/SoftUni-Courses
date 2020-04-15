class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self._radius = diameter / 2
        self._diameter = diameter

    def calculate_circumference(self):
        return Circle.__pi * self._diameter

    def calculate_area(self):
        return self.__pi * self._radius * self._radius

    def calculate_area_of_sector(self, angle):
        return self.calculate_area() * (angle / 360)

angle = 5
circle = Circle(10)

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")