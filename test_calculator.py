import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertNotEqual(add(1, -4), -5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4, -2), 6)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertNotEqual(subtract(1, 5), 6)
    ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 20), 4)
        self.assertEqual(div(-2, 10), -5)
    ##########################

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 1), 0.0)
        self.assertAlmostEqual(logarithm(2,8), 3.0)
        self.assertAlmostEqual(logarithm(0.25, 2), -2.0)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(2), 1.41421356)
        with self.assertRaises(ValueError):
            square_root(-4)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()