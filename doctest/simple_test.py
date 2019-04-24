#!/usr/bin/env python3

__copyright__ = "Muchen Sun: sunmch15@lzu.edu.cn"
__license__ = "MIT"
__version__ = "0.1"

def simple_func(x):
    """
    test 1: list
    >>> x = [1, 2, 3]
    >>> simple_func(x)
    12

    test 2: tuple
    >>> x = (1, 2, 3)
    >>> simple_func(x)
    Traceback (most recent call last):
    	...
    TypeError: Oh! Not tuple!
    """
    if isinstance(x, tuple):
        raise TypeError("Oh! Not tuple!")
    else:
        return 2 * sum(x)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
