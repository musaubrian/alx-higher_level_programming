#!/usr/bin/python3

"""Defines `inherits_from` that checks object inherits from a class"""

def inherits_from(obj, a_class):
    """
    Return:
        True if the object is an instance of a class that inherited (directly or indirectly) from @a_class
        else:
            False
    Args:
        @obj
        @a_class
    """
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)
