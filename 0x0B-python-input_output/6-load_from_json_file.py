#!/usr/bin/python3
"""
Module contains `load_from_json_file(...)` function
"""
import json


def load_from_json_file(filename):
    """
    creates an object from a json file
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
