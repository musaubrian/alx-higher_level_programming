#!/usr/bin/python3

"""define function `is_same_class`"""


def is_same_class(obj, a_class):
    """
    Args:
        @obj instance of a class
        @a_class class being checked
    Returns:
        True if object is exactly an instance of specified class
        False if it is not not an instance of specified class
    """
    return type(obj) is a_class
