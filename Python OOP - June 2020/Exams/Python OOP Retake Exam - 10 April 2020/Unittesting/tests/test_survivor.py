from project.survivor import Survivor
import unittest


class TestSurvivor(unittest.TestCase):
    def setUp(self):
        self.gosho = Survivor('Gosho', 5)

    def test_one(self):
        result = (self.gosho.name, self.gosho.age, self.gosho.needs, self.gosho.health)
        expected = ('Gosho', 5, 100, 100)
        self.assertEqual(result, expected)

        self.assertFalse(self.gosho.needs_healing)
        self.assertFalse(self.gosho.needs_sustenance)

    def test_two(self):
        with self.assertRaises(ValueError):
            self.gosho.name = ''
        self.gosho.name = 'Petko'
        self.assertEqual(self.gosho.name, 'Petko')

        with self.assertRaises(ValueError):
            self.gosho.age = -1
        self.gosho.age = 20
        self.assertEqual(self.gosho.age, 20)

    def test_three(self):
        with self.assertRaises(ValueError):
            self.gosho.health = -5
        self.gosho.health = 5
        self.assertEqual(self.gosho.health, 5)

        with self.assertRaises(ValueError):
            self.gosho.needs = -5
        self.gosho.needs = 5
        self.assertEqual(self.gosho.needs, 5)

        self.assertTrue(self.gosho.needs_healing)
        self.assertTrue(self.gosho.needs_sustenance)

if __name__ == '__main__':
    unittest.main()