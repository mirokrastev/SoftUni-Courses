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
        Tests insert method if it works as expected.
        """
        test_var = IntegerList(1, 2, 3)
        test_var.insert(2, 1)
        self.assertEqual(test_var.get_data(), [1, 2, 1, 3])

    def test_three(self):
        """
        Tests insert method if it raises an Exception when inserting to non existing index.
        """
        test_var = IntegerList(88, 3, 4)
        with self.assertRaises(IndexError):
            test_var.insert(5, 5)

    def test_four(self):
        """
        Tests insert method if it raises an Exception when inserting non int element.
        """
        test_var = IntegerList(88, 3, 4)
        with self.assertRaises(ValueError):
            test_var.insert(1, 'asd')

    def test_five(self):
        """
        Tests get_biggest method if it returns the biggest element.
        """
        test_var = IntegerList(2, 5, 100, 99, 100, 101, 107, 9)
        result = test_var.get_biggest()
        self.assertEqual(result, 107)

    def test_six(self):
        """
        Tests get_index method if it returns the index of arg element.
        """
        test_var = IntegerList(2, 5, 107, 9)
        result = test_var.get_index(2)
        self.assertEqual(result, 0)

    def test_seven(self):
        """
        Tests get_index method if it raises an Exception when returning non existing element.
        """
        test_var = IntegerList(2, 5, 107, 9)
        with self.assertRaises(Exception):
            test_var.get_index(55)

    def test_eight(self):
        """
        Tests get_biggest method if it raises an Exception when returning non existing element.
        """
        test_var = IntegerList()
        with self.assertRaises(Exception):
            test_var.get_biggest()

if __name__ == '__main__':
    unittest.main()