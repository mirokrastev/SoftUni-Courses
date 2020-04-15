class Town:
    def __init__(self, name):
        self.name = name

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f'Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}'