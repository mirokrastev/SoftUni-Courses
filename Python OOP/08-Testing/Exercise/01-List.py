import unittest

class Test(unittest.TestCase):
    def test_one(self):
        """
        Tests init method
        """
        test_var = IntegerList(1, 5, 10, 'asd', 6, 'qwe')
        self.assertEqual(test_var.get_data(), [1, 5, 10, 6])

    def test_two(self):
        """
        Tests add method if it appends and returns an list.
        """
        test_var = IntegerList()
        test_var.add(5)
        self.assertEqual(test_var.get_data(), [5])

    def test_three(self):
        """
        Tests add method if it raises an Exception when appending non int.
        """
        test_var = IntegerList(1, 10)
        with self.assertRaises(Exception):
            test_var.add('a')

    def test_four(self):
        """
        Tests remove method if it removes the element on that index and returns it.
        """
        test_var = IntegerList(54, 100, 2, 61, 2)
        result = test_var.remove_index(3)
        self.assertEqual(result, 61)

    def test_five(self):
        """
        Tests remove method if it raises an Exception when removing non existing item.
        """
        test_var = IntegerList(54, 100, 2, 61, 2)
        with self.assertRaises(Exception):
            test_var.remove_index(10)

    def test_six(self):
        """
        Tests get method if it returns specific element.
        """
        test_var = IntegerList(10, 11, 25, 2, 0)
        result = test_var.get(4)
        self.assertEqual(result, 0)

    def test_seven(self):
        """
        Tests get method if it raises an Exception when returning non existing element.
        """
        test_var = IntegerList(10, 11, 25, 2, 0)
        with self.assertRaises(Exception):
            test_var.get(7)


if __name__ == '__main__':
    unittest.main()