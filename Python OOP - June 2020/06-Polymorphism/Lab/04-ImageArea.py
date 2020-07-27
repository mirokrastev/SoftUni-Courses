class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, obj):
        return self.get_area() == obj.get_area()

    def __ne__(self, obj):
        return self.get_area() != obj.get_area()

    def __lt__(self, obj):
        return self.get_area() < obj.get_area()

    def __gt__(self, obj):
        return self.get_area() > obj.get_area()

    def __le__(self, obj):
        return self.get_area() <= obj.get_area()

    def __ge__(self, obj):
        return self.get_area() >= obj.get_area()