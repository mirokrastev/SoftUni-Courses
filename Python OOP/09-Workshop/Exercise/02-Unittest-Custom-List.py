import unittest

class Test(unittest.TestCase):
    def test_one(self):
        """
        Tests init method.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        self.call_var = self.custom_list.custom_list
        self.assertEqual(self.call_var, [1, 2, 3, 4])

    def test_two(self):
        """
        Tests append method if it appends to the end of the list and returns the list.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        test = self.custom_list.append(5)
        self.assertEqual(test, [1, 2, 3, 4, 5])

    def test_three(self):
        """
        Tests remove method if it removes the value on the index.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        self.call_var = self.custom_list.custom_list
        self.custom_list.remove(1)
        self.assertEqual(self.call_var, [1, 3, 4])

    def test_four(self):
        """
        Tests remove method if it removes the value on the index and returns it.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        element = self.custom_list.remove(1)
        self.assertEqual(element, 2)

    def test_five(self):
        """
        Tests get method if it gets the value on the index.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        element = self.custom_list.get(3)
        self.assertEqual(element, 4)

    def test_six(self):
        """
        Tests extend method if it appends the iterable to the list.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        self.call_var = self.custom_list.custom_list
        self.custom_list.extend([5, 6, 7])
        self.assertEqual(self.call_var, [1, 2, 3, 4, 5, 6, 7])

    def test_seven(self):
        """
        Tests extend method if it appends the iterable to the list and returns the list..
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        element = self.custom_list.extend([5, 6, 7])
        self.assertEqual(element, [1, 2, 3, 4, 5, 6, 7])

    def test_eight(self):
        """
        Tests insert method if it inserts the value on the specific index.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        self.call_var = self.custom_list.custom_list
        self.custom_list.insert(0, 5)
        self.assertEqual(self.call_var, [5, 1, 2, 3, 4])

    def test_nine(self):
        """
        Tests insert method if it inserts the value on the specific index and returns the list.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        element = self.custom_list.insert(0, 5)
        self.assertEqual(element, [5, 1, 2, 3, 4])

    def test_ten(self):
        """
        Tests pop method if it removes the last value.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        self.call_var = self.custom_list.custom_list
        self.custom_list.pop()
        self.assertEqual(self.call_var, [1, 2, 3])

    def test_eleven(self):
        """
        Tests pop method if it removes the last value and returns it..
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        element = self.custom_list.pop()
        self.assertEqual(element, 4)

    def test_twelve(self):
        """
        Tests clear method if it removes all the values, contained in the list.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        self.call_var = self.custom_list.custom_list
        self.custom_list.clear()
        self.assertEqual(self.call_var, [])

    def test_thirteen(self):
        """
        Tests index method if it returns the index of the given value.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        element = self.custom_list.index(2)
        self.assertEqual(element, 1)

    def test_fourteen(self):
        """
        Tests count method if it returns the number of times the value is contained in the list.
        """
        self.custom_list = CustomList(1, 2, 3, 4, 2, 3, 2)
        element = self.custom_list.count(2)
        self.assertEqual(element, 3)

    def test_fifteen(self):
        """
        Tests reverse method if it returns the values of the list in reverse order.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        self.call_var = self.custom_list.reverse()
        self.assertEqual(self.call_var, [4, 3, 2, 1])

    def test_sixteen(self):
        """
        Tests copy method if it returns a copy of the list.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        self.call_var = self.custom_list
        result = self.custom_list.reverse()
        self.assertFalse(self.call_var is result)

    def test_seventeen(self):
        """
        Tests size method if it returns the length of the list.
        """
        self.custom_list = CustomList(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(self.custom_list.size(), 7)

    def test_eighteen(self):
        """
        Tests add_first method if it adds the value at the beginning of the list.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        self.call_var = self.custom_list.custom_list
        self.custom_list.add_first(5)
        self.assertEqual(self.call_var, [5, 1, 2, 3, 4])

    def test_nineteen(self):
        """
        Tests dictionize method if it returns the list as a dictionary.
        """
        self.custom_list = CustomList(1, 2, 3, 4, 5, 6, 7, 8)
        element = self.custom_list.dictionalize()
        actual = {1: 2, 3: 4, 5: 6, 7: 8}
        self.assertEqual(element, actual)

    def test_twenty(self):
        """
        Tests move method if it moves the first amount of values to the end of the list.
        """
        self.custom_list = CustomList(1, 2, 3, 4, 5, 6, 7, 8)
        self.list_var = self.custom_list.custom_list
        self.custom_list.move(3)
        self.assertEqual(self.list_var, [4, 5, 6, 7, 8, 1, 2, 3])

    def test_twenty_one(self):
        """
        Tests move method if it moves the first amount of values to the end of the list and returns it.
        """
        self.custom_list = CustomList(1, 2, 3, 4, 5, 6, 7, 8)
        element = self.custom_list.move(3)
        self.assertEqual(element, [4, 5, 6, 7, 8, 1, 2, 3])

    def test_twenty_two(self):
        """
        Tests sum method if it returns the sum of the list with integers only.
        """
        self.custom_list = CustomList(1, 2, 3, 4)
        element = self.custom_list.sum()
        self.assertEqual(element, 10)

    def test_twenty_three(self):
        """
        Tests sum method if it returns the sum of the list with integers and strings.
        """
        self.custom_list = CustomList(1, 2, 3, 4, 'asd', 'test')
        element = self.custom_list.sum()
        self.assertEqual(element, 17)

    def test_twenty_four(self):
        """
        Tests overbound method if it returns the index of the biggest value.
        """
        self.custom_list = CustomList(1, 2, 7, 6, 5, 6)
        element = self.custom_list.overbound()
        self.assertEqual(element, 2)

    def test_twenty_five(self):
        """
        Tests underbound method if it returns the index of the smallest value.
        """
        self.custom_list = CustomList(1, 2, 7, 6, 5, 6)
        element = self.custom_list.underbound()
        self.assertEqual(element, 0)


if __name__ == '__main__':
    unittest.main()