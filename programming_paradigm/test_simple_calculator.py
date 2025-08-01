import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self. assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-2, 5), -7)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)
        self.assertEqual(self.calc.multiply(9, 2), 18)

    def test_division(self):
        self.assertEqual(self.calc.divide(4, 4), 1)
        self.assertEqual(self.calc.divide(8, 2), 4)

if __name__ == "__main__":
    unittest.main()

