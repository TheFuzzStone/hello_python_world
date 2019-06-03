import unittest
from employee import Employee

class TestForEmployee(unittest.TestCase):
    """Test for 'Employee' class."""

    def setUp(self):
        """A 'setUp' method for this test."""
        self.test_employee = Employee('john', 'doe', 70000)

    def test_give_default_raise(self):
        """Defaulr raise works correctly?"""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.salary, 75000)

    def test_give_custom_raise(self):
        """Custom raise works correctly?"""
        self.test_employee.give_raise(30000)
        self.assertEqual(self.test_employee.salary, 100000)

unittest.main()
