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
