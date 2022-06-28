#!/usr/bin/python3
"""
This module indents text passed as argument
"""

def text_indentation(text):
    """Prints text with 2 new lines after,
    ``. ? and :```
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i, j = 0, 0
    for a, char in enumerate(text):
        if char in ('.', '?', ':'):
            print(text[i:j], end="\n\n")
            i = j + 2
        else:
            if j == len(text) - 1:
                print(text[i:], end="")
        j += 1
