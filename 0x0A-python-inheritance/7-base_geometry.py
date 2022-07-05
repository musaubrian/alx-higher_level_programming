#!/usr/bin/python3
"""
Module contains `BaseGeometry` class
"""

class BaseGeometry:
    """
    Base class for geometry objects
    """

    def area(self):
        """
        Calculates area of the geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks if @value is an integer or not
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
