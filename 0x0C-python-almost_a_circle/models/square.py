#!/usr/bin/python3
"""defines class square which inherits class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    define square that inherits the class Rectangle attributes
    """
    def __init__(self, size, x=0, y=0, id=None) -> None:
        """
        initialize the square object
        Args:
            @size: (int) lenght/width of the square
            @x(int), @y(int), @id(int)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets size of the square"""
        return self.height

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
