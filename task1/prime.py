from typing import List


class PrimeHandler:
    """ this is a prime numbers class handler """
    @staticmethod
    def find_all_primes(num: int) -> List[int]:
        """
        this function will gets a number and returns all prime numbers that are lower
        >>> PrimeHandler.find_all_primes(6)
        [1, 2, 3, 5]
        >>> PrimeHandler.find_all_primes(13)
        [1, 2, 3, 5, 7, 11, 13]
        """
        primes = []
        for i in range(num):
            if PrimeHandler.is_prime(i + 1):
                primes.append(i + 1)
        return primes

    @staticmethod
    def is_prime(num: int) -> bool:
        """
        this function gets an integer and returns true if it's prime and false if it's not
        >>> PrimeHandler.is_prime(5)
        True
        >>> PrimeHandler.is_prime(9)
        False
        """
        dividers = []
        for i in range(num):
            if num % (i + 1) == 0:
                dividers.append(i + 1)

        if len(dividers) > 2:
            return False

        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
