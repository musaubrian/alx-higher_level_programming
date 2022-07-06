#!/usr/bin/python3
"""
module contains the function `append_write()`
"""


def append_write(filename="", text=""):
    """
    the functions appends text to an existing file
    Args:
        @filename: the name of the file
        @text: text being manipulated
    """
    with open(filename, "a", encoding="utf-8") as file:
        no_of_characters = file.write(text)
    return no_of_characters
