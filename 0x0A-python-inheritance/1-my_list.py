#!/usr/bin/python3

"""Defines MyList class that inherits from class list"""

class MyList(list):
    """Subclass of the class list"""

    def print_sorted(self):
        """
        Prints list in ascending order
        """
        print(sorted(self))
