import unittest


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.akaunt = Account('Ivan', 20)

    def test_one(self):
        result = (self.akaunt.owner, self.akaunt.amount, self.akaunt.balance, self.akaunt._transactions)
        expected = ('Ivan', 20, 20, [])
        self.assertEqual(result, expected)

    def test_two(self):
        with self.assertRaises(ValueError):
            self.akaunt.add_transaction('hello')
        self.akaunt.add_transaction(5)
        self.assertEqual(self.akaunt._transactions, [5])
        self.assertEqual(self.akaunt.balance, 25)

    def test_three(self):
        vtori_akaunt = Account('Gosho', 0)
        vtori_akaunt.add_transaction(-20)
        with self.assertRaises(ValueError):
            vtori_akaunt.validate_transaction(vtori_akaunt, -20)

        self.akaunt.add_transaction(10)
        self.assertEqual(self.akaunt.validate_transaction(self.akaunt, 10), f'New balance: {self.akaunt.balance}')
        self.assertEqual(self.akaunt.balance, 40)
        self.assertEqual(self.akaunt._transactions, [10, 10])

    def test_four(self):
        self.akaunt.add_transaction(20)
        self.assertEqual(len(self.akaunt), 1)

        self.assertEqual(self.akaunt[0], 20)

    def test_five(self):
        self.akaunt.add_transaction(20)
        self.akaunt.add_transaction(13)

        vtori_akaunt = Account('Gosho', 0)
        vtori_akaunt.add_transaction(3)
        vtori_akaunt.add_transaction(7)

        self.assertFalse(self.akaunt == vtori_akaunt)
        self.assertTrue(self.akaunt != vtori_akaunt)
        self.assertFalse(self.akaunt < vtori_akaunt)
        self.assertTrue(self.akaunt > vtori_akaunt)
        self.assertFalse(self.akaunt <= vtori_akaunt)
        self.assertTrue(self.akaunt >= vtori_akaunt)

        self.assertEqual(list(reversed(self.akaunt)), [13, 20])
        self.assertEqual(list(reversed(vtori_akaunt)), [7, 3])

        result = str(self.akaunt)
        expected = f'Account of Ivan with starting amount: 20'
        self.assertEqual(result, expected)

        result = str(vtori_akaunt)
        expected = f'Account of Gosho with starting amount: 0'
        self.assertEqual(result, expected)

        result = repr(self.akaunt)
        expected = f'Account(Ivan, 20)'
        self.assertEqual(result, expected)

        result = repr(vtori_akaunt)
        expected = f'Account(Gosho, 0)'
        self.assertEqual(result, expected)

    def test_six(self):
        vtori_akaunt = Account('Gosho', 0)
        self.akaunt.add_transaction(10)
        vtori_akaunt.add_transaction(55)
        treti_akaunt = self.akaunt + vtori_akaunt

        self.assertEqual(treti_akaunt._transactions, [10, 55])
        self.assertEqual(treti_akaunt._transactions, [10, 55])

    def test_seven(self):
        test_account_1 = Account('Spiridon Bahurov')
        test_account_1.add_transaction(10)
        test_account_2 = Account('Vergiliy Gerasimov')
        test_account_2.add_transaction(10)
        self.assertFalse(test_account_1 > test_account_2)
        self.assertTrue(test_account_1 >= test_account_2)
        self.assertFalse(test_account_1 < test_account_2)
        self.assertTrue(test_account_1 <= test_account_2)
        self.assertFalse(test_account_1 != test_account_2)
        self.assertTrue(test_account_1 == test_account_2)


if __name__ == '__main__':
    unittest.main()