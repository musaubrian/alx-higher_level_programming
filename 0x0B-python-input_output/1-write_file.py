#!/usr/bin/python3
"""
Module contains the function `write_file(...)`
"""


def write_file(filename="", text=""):
    """
    function writes a string to a text file in utf-8 encoding
    Returns:
        number of characters
    """
    with open(filename, "w") as file:
        no_of_characters = file.write(text)
    return no_of_characters
