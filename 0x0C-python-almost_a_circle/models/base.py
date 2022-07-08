#!/usr/bin/python3
"""
module `base` contains class base
"""


class Base:
    """
    Base of all other classes
    Manages `id` attribute of all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize class instance
        Args:
            @id: value of each new class instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
