#!/usr/bin/python3
"""
module contains function `append_after(...)`
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        @filename: name of the file(str)
        @search_string: string to search for(str)
        @new_string: string to be appended(str)
    """

    text = ""
    with open(filename, encoding="utf-8") as read_file:
        for line in read_file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as write_to_file:
        write_to_file.write(text)
