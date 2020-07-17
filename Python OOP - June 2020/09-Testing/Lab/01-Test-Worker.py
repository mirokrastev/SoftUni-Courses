import unittest

class WorkerTests(unittest.TestCase):
    def test_one(self):
        """
         Test if the worker is initialized with correct name, salary and energy
        """
        name = 'Test Name'
        salary = 1000
        energy = 5
        worker = Worker(name, salary, energy)
        self.assertEqual(worker.name, name)
        self.assertEqual(worker.salary, salary)
        self.assertEqual(worker.energy, energy)

    def test_two(self):
        """
        Test if the worker's energy is incremented after the rest method is called
        """
        name = 'Test Name'
        salary = 1000
        energy = 5
        worker = Worker(name, salary, energy)
        worker.rest()
        self.assertEqual(worker.energy, energy+1)

    def test_three(self):
        """
        Test if an error is raised if the worker tries to work with negative energy or equal to 0
        """
        name = 'Test Name'
        salary = 1000
        energy = 0
        worker = Worker(name, salary, energy)
        with self.assertRaises(Exception):
            worker.work()

    def test_four(self):
        """
        Test if the worker's money is increased by his salary correctly after the work method is called
        """
        name = 'Test Name'
        salary = 1000
        energy = 55
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.money, worker.salary)
        worker.work()
        self.assertEqual(worker.money, worker.salary * 2)

    def test_five(self):
        """
        Test if the worker's energy is decreased after the work method is called
        """
        name = 'Test Name'
        salary = 1000
        energy = 5
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.energy, energy-1)

    def test_six(self):
        """
        Test if the get_info method returns the proper string with correct values
        """
        name = 'Test Name'
        salary = 1000
        energy = 5
        worker = Worker(name, salary, energy)
        info = worker.get_info()
        expected_info = f'{worker.name} has saved 0 money.'
        self.assertEqual(info, expected_info)

if __name__ == '__main__':
    unittest.main()