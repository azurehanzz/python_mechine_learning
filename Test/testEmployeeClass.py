import unittest
from EmployeeClass import Employee

class Employeetestcase(unittest.TestCase):
    def setUp(self):
        self.Employee1 = Employee('jing','han')

    def test_give_default_raise(self):
        self.Employee1.give_raise()
        self.assertEqual(self.Employee1.salary,10000)

    def test_give_random_raise(self):
        self.Employee1.give_raise(3000)
        self.assertEqual(self.Employee1.salary,8000)

if __name__ == 'main':
    unittest.main()
