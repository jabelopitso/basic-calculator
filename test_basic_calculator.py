import unittest
from basic_calculator import *

class TestBasicCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(division(10, 2), 5)
        self.assertAlmostEqual(division(7, 3), 2.3333, places=4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
