#!/usr/bin/python3
"""
Module that inherits `BaseGeometry` class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """
    Geometry object from inherited class BaseGeometry 
    """

    def __init__(self, width, height) -> None:
        """
        initialize new rectangle geometry object
        with given @height nad @width
        Args:
            @height: height of the rectangle
            @width: width of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Finds area
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """
        return representation of the rectangle object
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
