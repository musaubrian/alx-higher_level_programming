#!/usr/bin/python3
"""
module contains class `Rectangle`
"""
from models.base import Base as BaseClass


class Rectangle(BaseClass):
    """
    defines a Rectangle that inherits from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """
        initialize Rectangle instance
        Args:
            @width: width of the Rectangle
            @height: heightof the rectangle
            @x
            @y
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y
