#!/usr/bin/python3
"""
module `base` contains class base
"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return:
            JSON representation of an object string
        Args:
            list_dictionary: list of dictionaries(list)
        """
        if list_dictionaries is None:
            return "[]"

        json_dump = json.dumps(list_dictionaries)
        return json_dump

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        Args:
            @list_objs: (list) list of instances inheriting Base
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))
