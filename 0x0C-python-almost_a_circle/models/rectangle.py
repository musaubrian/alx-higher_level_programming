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


    @property
    def width(self):
        """getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width attribute"""
        self.__width = value

    @property
    def height(self):
        """
        getter method for height attribute
        return:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height attribute"""
        self.__height = value
    
    @property
    def x(self):
        """
        getter method for x attribute
        return:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x attribute"""
        self.__x = value

    @property
    def y(self):
        """
        getter method for y attribute
        return:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y attribute"""
        self.__y = value
