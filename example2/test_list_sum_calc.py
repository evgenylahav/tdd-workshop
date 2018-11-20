import unittest
from example2.list_sum_calc import list_sum_calc


class TestListSumCalc(unittest.TestCase):
    def test_empty_inputs(self):
        with self.assertRaises(TypeError):
            list_sum_calc()

    def test_non_int_inputs(self):
        with self.assertRaises(TypeError):
            list_sum_calc('5', 7)

    def test_min_0_max_1(self):
        self.assertEqual(list_sum_calc(0, 1), 1)

    def test_min_1_max_4(self):
        self.assertEqual(list_sum_calc(1, 4), 10)

    def test_min_5_max_10(self):
        self.assertEqual(list_sum_calc(5, 10), 45)

    def test_min_10_max_5(self):
        with self.assertRaises(ValueError):
            list_sum_calc(10, 5)

    def test_min_7_max_7(self):
        self.assertEqual(list_sum_calc(7, 7), 7)
