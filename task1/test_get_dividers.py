import unittest
from task1.get_dividers import get_dividers


class TestGetDividers(unittest.TestCase):

    def test_zero(self):
        with self.assertRaises(ValueError):
            get_dividers(0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            get_dividers(-5)

    def test_one(self):
        self.assertEqual(get_dividers(1), [1])

    def test_small_prime(self):
        self.assertEqual(get_dividers(5), [5])

    def test_large_prime(self):
        self.assertEqual(get_dividers(31), [31])

    def test_6(self):
        self.assertEqual(get_dividers(6), [2, 3])

    def test_12(self):
        self.assertEqual(get_dividers(12), [2, 2, 3])

    def test_50(self):
        self.assertEqual(get_dividers(50), [2, 5, 5])

    def test_63(self):
        self.assertEqual(get_dividers(63), [3, 3, 7])
