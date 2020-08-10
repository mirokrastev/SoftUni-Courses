import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.ll = IntegerList(1, 2, 3, 4)

    def test_one(self):
        self.assertEqual(self.ll.get_data(), [1, 2, 3, 4])

    def test_two(self):
        with self.assertRaises(ValueError):
            self.ll.add('a')
        self.assertEqual(self.ll.add(5), [1, 2, 3, 4, 5])

    def test_three(self):
        with self.assertRaises(IndexError):
            self.ll.remove_index(7)
        self.assertEqual(self.ll.remove_index(0), 1)

    def test_four(self):
        with self.assertRaises(IndexError):
            self.ll.get(6)
        self.assertEqual(self.ll.get(1), 2)

    def test_five(self):
        with self.assertRaises(IndexError):
            self.ll.insert(6, 4)
        with self.assertRaises(ValueError):
            self.ll.insert(2, 'a')
        self.ll.insert(0, 6)
        self.assertEqual(self.ll.get_data(), [6, 1, 2, 3, 4])

    def test_six(self):
        self.assertEqual(self.ll.get_biggest(), 4)
        self.assertEqual(self.ll.get_index(2), 1)


if __name__ == '__main__':
    unittest.main()