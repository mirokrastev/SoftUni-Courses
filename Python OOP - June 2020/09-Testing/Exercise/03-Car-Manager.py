import unittest

class Test(unittest.TestCase):
    def test_one(self):
        """
        Tests init method.
        """
        car = Car('a4', 'audi', 7, 60)
        car_make = car.make
        car_model = car.model
        car_fuel_consmp = car.fuel_consumption
        car_fuel_capacity = car.fuel_capacity
        self.assertEqual(car_make, 'a4')
        self.assertEqual(car_model, 'audi')
        self.assertEqual(car_fuel_consmp, 7)
        self.assertEqual(car_fuel_capacity, 60)

    def test_two(self):
        """
        Tests car.make setter for new property which raises an Exception when is empty.
        """
        car = Car('a4', 'audi', 7, 60)
        with self.assertRaises(Exception):
            car.make = ''

    def test_three(self):
        """
        Tests car.model setter for new property which raises an Exception when is empty.
        """
        car = Car('a4', 'audi', 7, 60)
        with self.assertRaises(Exception):
            car.model = ''

    def test_four(self):
        """
        Tests car.fuel_consumption setter for new property which raises an Exception when is below 0.
        """
        car = Car('a4', 'audi', 7, 60)
        with self.assertRaises(Exception):
            car.fuel_consumption = -5

    def test_five(self):
        """
        Tests car.fuel_capacity setter for new property which raises an Exception when is below 0.
        """
        car = Car('a4', 'audi', 7, 60)
        with self.assertRaises(Exception):
            car.fuel_capacity = -1

    def test_six(self):
        """
        Tests car.fuel_amount setter.
        """
        car = Car('a4', 'audi', 7, 60)
        self.assertEqual(car.fuel_amount, 0)
        car.fuel_amount = 20
        self.assertEqual(car.fuel_amount, 20)

    def test_seven(self):
        """
        Tests car.fuel_amount setter for new property which raises an Exception when is empty.
        """
        car = Car('a4', 'audi', 7, 60)
        with self.assertRaises(Exception):
            car.fuel_capacity = -1

    def test_eight(self):
        """
        Tests car.refuel method if it raises an Exception when arg is 0 or below.
        """
        car = Car('a4', 'audi', 7, 60)
        with self.assertRaises(Exception):
            car.refuel(-2)

    def test_nine(self):
        """
        Tests car.refuel method if it refuels normally.
        """
        car = Car('a4', 'audi', 7, 60)
        self.assertEqual(car.fuel_amount, 0)
        car.refuel(5)
        self.assertEqual(car.fuel_amount, 5)

    def test_ten(self):
        """
        Tests car.refuel method if it works normally when fuel_amount is more than fuel_capacity.
        """
        car = Car('a4', 'audi', 7, 60)
        car.fuel_amount = 55
        self.assertEqual(car.fuel_amount, 55)
        car.refuel(10)
        self.assertEqual(car.fuel_amount, 60)

    def test_eleven(self):
        """
        Tests car.drive method if it works normally.
        """
        car = Car('a4', 'audi', 7, 60)
        car.refuel(40)
        car.drive(5)
        self.assertEqual(car.fuel_amount, 39.65)

    def test_twelve(self):
        """
        Tests car.drive method if it raises an Exception when needed fuel consumption is bigger than car.fuel_amount.
        """
        car = Car('a4', 'audi', 999, 60)
        car.refuel(4)
        with self.assertRaises(Exception):
            car.drive(500)


if __name__ == '__main__':
    unittest.main()