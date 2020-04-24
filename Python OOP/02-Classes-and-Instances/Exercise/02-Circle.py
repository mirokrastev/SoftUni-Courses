class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return round(self.radius * self.radius * Circle.pi, 2)

    def get_circumference(self):
        return 2 * Circle.pi * self.radius