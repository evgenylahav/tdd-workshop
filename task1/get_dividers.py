from typing import List
from task1.prime import PrimeHandler


def get_dividers(num: int) -> List[int]:
    """
    this function will get an input number and will return all its
    primary dividers.
    for num < 0 a ValueError will be raised
    for num = 1 the result is 1
    for all other cases, the result will contain all the prime dividers excluding 1

    >>> get_dividers(6)
    [2, 3]

    >>> get_dividers(10)
    [2, 5]

    """
    if num <= 0:
        raise ValueError

    if num == 1:
        return [1]

    if PrimeHandler.is_prime(num):
        return [num]

    return _find_dividers(num)


def _find_dividers(num: int) -> List[int]:
    """
    this function will return the prime dividers of a number
    """

    dividers: List[int] = list()
    while num != 1:
        primes = PrimeHandler.find_all_primes(num)
        for prime in reversed(primes):
            if num % prime == 0:
                dividers.append(prime)
                num = num // prime
                break
    return list(reversed(dividers))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
