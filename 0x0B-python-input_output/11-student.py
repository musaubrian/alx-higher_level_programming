#!/usr/bin/python3
"""
Class Student defining a student
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return:
            dictionary representation of a student instance
        """
        if type(attrs) is list and all(type(s) is str for s in attrs):
            response = {}
            for key in attrs:
                if key in self.__dict__:
                    response[key] = self.__dict__[key]
            return response
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of student instance
        """
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
