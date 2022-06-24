#!/usr/bin/python3

"""
This module ``3-say_my_name`` prints the first and last name of a person
"""
def say_my_name(first_name, last_name=""):
    """
    print first name and last name

    format:
        My name is first_name last_name

    Args:
        first_name(str)
        last_name(str)

    raise TypeError:
        when first_name or second_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
