#!/usr/bin/python3

""" MOdule defines rectangle using class Rectangle """

class Rectangle:
    """defines a rectangle """
    def __init__(self, width=0, height=0):
        """
        initialize the rectangle
        Args::
            width(type int): Width of the rectangle.
            height(type int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        return height of the rectangle
        """
        return self.height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Return:
            width of the rectangel
        """
        return self.width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
