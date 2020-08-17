import unittest
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.fabrika = PaintFactory('Qica', 2500)

    def test_one(self):
        result = (self.fabrika.name, self.fabrika.capacity, self.fabrika.ingredients)
        expected = ('Qica', 2500, {})

        self.assertEqual(result, expected)

    def test_two(self):
        with self.assertRaises(TypeError):
            self.fabrika.add_ingredient('test', 2000)

        with self.assertRaises(ValueError):
            self.fabrika.add_ingredient('white', 3000)

        self.fabrika.add_ingredient('white', 5)
        self.assertEqual(self.fabrika.products, {'white': 5})
        self.assertEqual(self.fabrika.capacity, 2495)

    def test_three(self):
        with self.assertRaises(KeyError):
            self.fabrika.remove_ingredient('test', 5)

        self.fabrika.add_ingredient('white', 5)

        with self.assertRaises(ValueError):
            self.fabrika.remove_ingredient('white', 6)

        self.fabrika.remove_ingredient('white', 2)
        self.assertEqual(self.fabrika.products, {'white': 3})

    def test_four(self):
        self.assertFalse(self.fabrika.can_add(5000))
        self.assertTrue(self.fabrika.can_add(10))


if __name__ == '__main__':
    unittest.main()