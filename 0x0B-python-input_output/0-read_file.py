#!/usr/bin/python3
"""
Contains the function `read_file()`
"""


def read_file(filename=""):
    """
    Reads a text file in the UTF-8 encoding
    and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            print(line)
