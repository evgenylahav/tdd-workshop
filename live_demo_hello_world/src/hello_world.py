""" hello world module """


def hello_world() -> str:
    """
    hello world function
    >>> hello_world()
    'Hello, world!'
    """
    return "Hello, world!"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
