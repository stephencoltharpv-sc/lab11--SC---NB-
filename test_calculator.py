# https://github.com/stephencoltharpv-sc/lab11--SC---NB-
# Partner 1: Stephen Coltharp
# Partner 2: Nishchay Bhattarai
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    # https://github.com/stephencoltharpv-sc/lab11--SC---NB-
    # Partner 1: Stephen Coltharp
    # Partner 2: Nishchay Bhattarai
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 5), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm( 10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 1), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)


    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)
    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, -2), -2)
        self.assertEqual(add(0, 0), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 2), 1)
        self.assertEqual(div(-2, -2), 1)
        self.assertEqual(div(8, 2), .25)


    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(4, 3), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(7, 24), 25)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(16), 4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
