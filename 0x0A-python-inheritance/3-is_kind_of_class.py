#!/usr/bin/python3

"""Defines `is_kind_of_class` that checks for kind of a class"""


def is_kind_of_class(obj, a_class):
    """
    returns:
        True if @obj is an instance of a class
            or
        instance of a class inherited from the specified class
        else:
            False
    Args:
        @obj: object being checked
        @a_class: specified class
    """
    return isinstance(obj, a_class)
