#!/usr/bin/python3

"""
define class square with private attribute ``size``,
and insaniates it.
"""

class Square:
    """
    define square with private attribute ``size``
    """
    def __init__(self, size):
        """
        Args:
            size: size of square.
        
        Attributes:
            size: Private instance.
    """
    self.__size = size
