import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
   
    def setUp(self):
        self.calc = Calculator()

    # Testy dla dodawania
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(2, -3), -1)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    # Testy dla odejmowania
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_mixed_sign_numbers(self):
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)

    # Testy dla mnożenia
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_mixed_sign_numbers(self):
        self.assertEqual(self.calc.multiply(2, -3), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_multiply_zero_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 0), 0)

    # Testy dla dzielenia
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_divide_mixed_sign_numbers(self):
        self.assertEqual(self.calc.divide(6, -3), -2)

    def test_divide_by_one(self):
        self.assertEqual(self.calc.divide(5, 1), 5)

    def test_divide_one_by_one(self):
        self.assertEqual(self.calc.divide(1, 1), 1)

    def test_divide_negative_by_positive(self):
        self.assertEqual(self.calc.divide(-6, 3), -2)

    def test_divide_positive_by_negative(self):
        self.assertEqual(self.calc.divide(6, -3), -2)

    # Test dzielenia przez zero
    def test_divide_by_zero_raises_exception(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    # Testy dla granicznych przypadków
    def test_add_large_numbers(self):
        self.assertEqual(self.calc.add(10**10, 10**10), 2 * 10**10)

    def test_subtract_large_numbers(self):
        self.assertEqual(self.calc.subtract(10**10, 10**9), 9 * 10**9)

    def test_multiply_large_numbers(self):
        self.assertEqual(self.calc.multiply(10**5, 10**5), 10**10)

    def test_divide_large_numbers(self):
        self.assertEqual(self.calc.divide(10**10, 10**5), 10**5)

    # Testy dla wartości zmiennoprzecinkowych
    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(0.5, 0.3), 0.2, places=7)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(0.5, 0.2), 2.5, places=7)

if __name__ == '__main__':
    unittest.main()