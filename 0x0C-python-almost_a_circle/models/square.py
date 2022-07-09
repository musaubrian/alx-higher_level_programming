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
        """setter method for size"""
        self.width = size
        self.height = size

    def __str__(self):
        """override __str__ of retcangle class"""
        return(
                f"[{self.__class__.__name__}] "
                f"({self.id}) {self.x}/{self.y} "
                f"- {self.width}"
                )

    def update(self, *args):
        """update square instance"""
        sq_arg_counter = 0
        for arg in args:
            if sq_arg_counter == 0:
                if arg is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = arg
            elif sq_arg_counter == 1:
                self.size = arg
            elif sq_arg_counter == 2:
                self.x = arg
            elif sq_arg_counter == 3:
                self.y = arg
            sq_arg_counter += 1
