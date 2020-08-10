import unittest


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Car(50, 7)
        self.truck = Truck(500, 30)

    def test_one(self):
        car_result = (self.car.fuel_quantity, self.car.fuel_consumption)
        car_expected = (50, 7)
        self.assertEqual(car_result, car_expected)

        truck_result = (self.truck.fuel_quantity, self.truck.fuel_consumption)
        truck_expected = (500, 30)
        self.assertEqual(truck_result, truck_expected)

    def test_two(self):
        self.car.drive(2)
        self.assertEqual(self.car.fuel_quantity, 34.2)

        self.truck.drive(2)
        self.assertEqual(self.truck.fuel_quantity, 436.8)

    def test_three(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_quantity, 60)

        self.truck.refuel(10)
        self.assertEqual(self.truck.fuel_quantity, 509.5)


if __name__ == '__main__':
    unittest.main()