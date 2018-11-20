import unittest
from task1.prime import PrimeHandler


class TestPrimeHandles(unittest.TestCase):
    def test_is_prime_2(self):
        self.assertEqual(PrimeHandler.is_prime(2), True)

    def test_is_prime_1(self):
        self.assertEqual(PrimeHandler.is_prime(1), True)

    def test_is_prime_5(self):
        self.assertEqual(PrimeHandler.is_prime(5), True)

    def test_is_prime_9(self):
        self.assertEqual(PrimeHandler.is_prime(9), False)

    def test_is_prime_neg_11(self):
        self.assertEqual(PrimeHandler.is_prime(-11), True)

    def test_is_prime_17(self):
        self.assertEqual(PrimeHandler.is_prime(17), True)

    def test_find_all_primes_small(self):
        self.assertEqual(PrimeHandler.find_all_primes(5), [1, 2, 3, 5])

    def test_find_all_primes_large(self):
        self.assertEqual(PrimeHandler.find_all_primes(15), [1, 2, 3, 5, 7, 11, 13])


