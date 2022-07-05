#!/usr/bin/python3
"""
Module contains class Square that inherits class Rectangle
"""

Rectangle = __import__("9.rectangle").Rectangle

class Square(Rectangle):
    """
    class Square defines a square geometry
    """

    def __init__(self, size) -> None:
        """
        Initialize a new square object
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Finds the area
        """
        return self.__size ** 2
