import unittest
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.kompiutur = Hardware('Pentium', 'Heavy', 1000, 1000)

    def test_one(self):
        result = (self.kompiutur.name, self.kompiutur.type, self.kompiutur.memory, self.kompiutur.capacity)
        expected = ('Pentium', 'Heavy', 1000, 1000)

        self.assertEqual(result, expected)

    def test_two(self):
        programa = Software('Test', 'Express', 2000, 2000)

        with self.assertRaises(Exception) as ex:
            self.kompiutur.install(programa)
        self.assertEqual(str(ex.exception), 'Software cannot be installed')

    def test_three(self):
        programa = Software('Test', 'Express', 5, 5)

        self.kompiutur.install(programa)
        self.kompiutur.uninstall(programa)

        self.assertListEqual([], self.kompiutur.software_components)


if __name__ == '__main__':
    unittest.main()