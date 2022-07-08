#!/usr/bin/python3
"""Module contains `class_to_json(...)` function"""


def class_to_json(obj):
    """
    Args:
        @obj: instance of a class
    Return:
        dictionary description
    """
    return obj.__dict__
