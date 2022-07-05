#!/usr/bin/python3
"""Defines a function that checks for kind of classes"""


def is_kind_of_class(obj, a_class):
    """
    return:
        True if @obj is instance of a class
            or if is an instance of a class inherited from sepecified class
            else:
                False

    Args:
        @obj
        @a_class
    """
    return isinstance((obj, a_class))
