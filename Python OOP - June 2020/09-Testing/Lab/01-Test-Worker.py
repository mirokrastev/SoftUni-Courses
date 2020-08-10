import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Pesho', 2000, 100)

    def test_one(self):
        name, salary, energy = (self.worker.name, self.worker.salary, self.worker.energy)
        self.assertEqual(name, 'Pesho')
        self.assertEqual(salary, 2000)
        self.assertEqual(energy, 100)

    def test_two(self):
        worker = Worker('Gosho', 1500, 90)
        self.assertEqual(worker.energy, 90)
        worker.rest()
        self.assertEqual(worker.energy, 91)

    def test_three(self):
        worker = Worker('Ivan', 100, 1)
        self.assertEqual(worker.energy, 1)
        worker.work()
        self.assertEqual(worker.energy, 0)
        with self.assertRaises(Exception):
            worker.work()

    def test_four(self):
        self.assertEqual(self.worker.money, 0)
        self.worker.work()
        self.assertEqual(self.worker.money, 2000)

    def test_six(self):
        string = self.worker.get_info()
        to_compare = f'{self.worker.name} has saved {self.worker.money} money.'
        self.assertEqual(string, to_compare)


if __name__ == '__main__':
    unittest.main()