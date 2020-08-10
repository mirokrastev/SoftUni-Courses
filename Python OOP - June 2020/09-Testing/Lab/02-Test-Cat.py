import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('kotka')

    def test_one(self):
        self.assertEqual(self.cat.size, 0)
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_two(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_three(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_four(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()