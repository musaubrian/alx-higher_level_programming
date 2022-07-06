#!/usr/bin/python3
"""
module contains the function `save_to_json_file(...)`
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes @my_obj to @filename
    Args:
        @my_obj: object
        @filename: name of the file being manipulated
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
