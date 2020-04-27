import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self): pass

    @abstractmethod
    def calculate_perimeter(self): pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius * self.radius * math.pi

    def calculate_perimeter(self):
        return 2 * self.radius * math.pi

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)