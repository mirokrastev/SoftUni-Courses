import unittest


class TestGroups(unittest.TestCase):
    def setUp(self):
        self.p_one = Person('Ivan', 'Ivanov')
        self.g_one = Group('Vipovete', [self.p_one])

    def test_one(self):
        result = str(self.p_one)
        expected = f'{self.p_one.name} {self.p_one.surname}'
        self.assertEqual(result, expected)

        p_two = Person('Ginka', 'Turkinqta')
        p_three = self.p_one + p_two

        result = str(p_three)
        expected = f'{p_three.name} {p_three.surname}'
        self.assertEqual(result, expected)

    def test_two(self):
        result = (self.g_one.name, self.g_one.people)
        expected = ('Vipovete', [self.p_one])
        self.assertEqual(result, expected)

    def test_three(self):
        self.assertEqual(len(self.g_one), 1)
        self.assertEqual(self.g_one[0], "Person 0: Ivan Ivanov")

        p_two = Person('Ginka', 'Turkinqta')
        p_three = self.p_one + p_two
        g_two = Group('Milionerite', [p_two, p_three])

        g_three = self.g_one + g_two
        result = (g_three.name, g_three.people)
        expected = (g_three.name, [self.p_one, p_two, p_three])
        self.assertEqual(result, expected)
        self.assertEqual(g_three[2], f'Person 2: {str(p_three)}')
        self.assertEqual(len(g_three), 3)

        result = (str(g_three))
        expected = f'Group {g_three.name} with members Ivan Ivanov, Ginka Turkinqta, Ivan Turkinqta'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()