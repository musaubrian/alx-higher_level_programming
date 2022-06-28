#!/usr/bin/python3

"""
This module ``4-print_square`` prints a square with the char ``#``
"""

def print_square(size):
    """
    print_square::
        prints a square using the ``#`` character

    args:
        size -> size length of the square

    raise:
        TypeError:
            if size is not an integer
        ValueError:
            if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if ((isinstance(size, float) and (size < 0))):
        raise TypeError("size must be an integer")
    for row in range(0, size):
        for col in range(0, size):
            print("#", end="")
        print()
