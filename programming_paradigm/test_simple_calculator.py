# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the addition method.
        """
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test zero
        self.assertEqual(self.calc.add(0, 0), 0)
        # Test large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """
        Test the subtraction method.
        """
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Test large numbers
        self.assertEqual(self.calc.subtract(2000000, 1000000), 1000000)

    def test_multiplication(self):
        """
        Test the multiplication method.
        """
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        # Test zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Test large numbers
        self.assertEqual(self.calc.multiply(1000, 2000), 2000000)

    def test_division(self):
        """
        Test the division method.
        """
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test zero divided by a number
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Test negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)
        # Test large numbers
        self.assertEqual(self.calc.divide(2000000, 1000000), 2)

if __name__ == "__main__":
    unittest.main()