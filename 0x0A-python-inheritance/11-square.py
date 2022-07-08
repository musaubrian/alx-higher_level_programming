#!/usr/bin/python3
"""
Module contains class Square that inherits class Rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    class Square defines a square geometry
    """

    def __init__(self, size) -> None:
        """
        Initialize a new square object
        Args:
            @size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        calculates area of the square
        """
        return self.__size ** 2

    def __str__(self) -> str:
        """
        return string representaion of the square object
        """
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
