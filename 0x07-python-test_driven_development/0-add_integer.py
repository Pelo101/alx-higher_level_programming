#!/usr/bin/python3
"""

This module computes and returns the summ of two numbers.

"""


def add_integer(a, b=98):
    """ Function computes the sum of two integers and or floats.

    Args:

    a: the first number
    b: the second number

    Raises:

    TypeError: if a and b is not an integer or float.

    Return:

    Sum of two numbers.

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
