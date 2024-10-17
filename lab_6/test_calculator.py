import unittest
from bll.operations import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.perform_calculation(2, 3, '+'), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.perform_calculation(5, 3, '-'), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.perform_calculation(2, 3, '*'), 6)

    def test_division(self):
        self.assertEqual(self.calc.perform_calculation(6, 3, '/'), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.perform_calculation(6, 0, '/')

    def test_square_root(self):
        self.assertEqual(self.calc.perform_calculation(9, None, '√'), 3)

if __name__ == "__main__":
    unittest.main()
