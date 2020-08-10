import unittest


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car('Peugeot', '206', 7, 80)

    def test_one(self):
        result = (self.car.make, self.car.model, self.car.fuel_consumption, self.car.fuel_capacity)
        expected = ('Peugeot', '206', 7, 80)
        self.assertEqual(result, expected)

    def test_two(self):
        with self.assertRaises(Exception):
            self.car.make = ''
        self.car.make = 'Audi'
        self.assertEqual(self.car.make, 'Audi')

    def test_three(self):
        with self.assertRaises(Exception):
            self.car.model = ''
        self.car.model = '207'
        self.assertEqual(self.car.model, '207')

    def test_four(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = ''
        self.car.fuel_consumption = 8
        self.assertEqual(self.car.fuel_consumption, 8)

        with self.assertRaises(Exception):
            self.car.fuel_capacity = -2
        self.car.fuel_capacity = 70
        self.assertEqual(self.car.fuel_capacity, 70)

        with self.assertRaises(Exception):
            self.car.fuel_amount = -1
        self.car.fuel_amount = 50
        self.assertEqual(self.car.fuel_amount, 50)

    def test_five(self):
        with self.assertRaises(Exception):
            self.car.refuel(-1)
        self.car.refuel(5)
        self.assertEqual(self.car.fuel_amount, 5)

    def test_six(self):
        self.car.refuel(5)
        with self.assertRaises(Exception):
            self.car.drive(5000)
        self.car.drive(2)
        self.assertEqual(self.car.fuel_amount, 4.86)


if __name__ == '__main__':
    unittest.main()