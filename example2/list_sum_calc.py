def list_sum_calc(min_value: int, max_value: int) -> int:
    """
    this function returns the sum of all values between min_value
    and max_value
    >>> list_sum_calc(1, 4)
    10
    >>> list_sum_calc(3, 5)
    12
    """
    if not isinstance(min_value, int) or not isinstance(max_value, int):
        raise TypeError

    if max_value < min_value:
        raise ValueError

    return sum([x for x in range(min_value, max_value + 1)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
