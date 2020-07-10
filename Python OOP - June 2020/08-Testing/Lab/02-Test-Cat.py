import unittest

class CatTests(unittest.TestCase):
    def test_one(self):
        """
        Cat's size is increased after eating
        """
        name = 'Tosho Kukata'
        kotka = Cat(name)
        self.assertEqual(kotka.size, 0)
        kotka.eat()

        self.assertEqual(kotka.size, 1)

    def test_two(self):
        """
        Cat is fed after eating
        """
        name = 'Tosho Kukata'
        kotka = Cat(name)
        kotka.eat()
        self.assertTrue(kotka.sleepy)

    def test_three(self):
        """
        Cat cannot eat if already fed, raises an error
        """
        name = 'Tosho Kukata'
        kotka = Cat(name)
        kotka.eat()
        with self.assertRaises(Exception):
            kotka.eat()

    def test_four(self):
        """
        Cat cannot fall asleep if not fed, raises an error
        """
        name = 'Tosho Kukata'
        kotka = Cat(name)
        with self.assertRaises(Exception):
            kotka.sleep()

    def test_five(self):
        """
        Cat is not sleepy after sleeping
        """
        name = 'Tosho Kukata'
        kotka = Cat(name)
        kotka.eat()
        kotka.sleep()
        self.assertFalse(kotka.sleepy)

if __name__ == '__main__':
    unittest.main()