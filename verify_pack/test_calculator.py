import unittest

from app.calculator import Calculator

class VerifyCalculatorTest(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        result = calculator.add(4,2)
        self.assertEqual(6,result)
    def test_minus(self):
        calculator = Calculator()
        result = calculator.substract(4,2)
        self.assertEqual(2, result)
    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(4,2)
        self.assertEqual(8, result)
    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(4,2)
        self.assertEqual(2, result)