#!/usr/bin/python3
"""
module contains `from_json_String(...)` function
"""
import json


def from_json_String(my_str):
    """
    Args:
        @my_str: JSON string
    Return:
        object represented by JSON string(@my_str)
    """
    load_json = json.loads(my_str)
    return load_json
