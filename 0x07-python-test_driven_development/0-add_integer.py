#!/usr/bin/python3

"""
    This is the ``add_integer`` module
    ==================================
    It defines addition between two integers
"""

def add_integer(a, b=98):
    """
    Fuction returns sum of a and b ``a + b``,
    with a and b being either integers or floats

    Raises TypeError:
        when a or b is not an integer or exact float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
