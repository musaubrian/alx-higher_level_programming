#!/usr/bin/python3
"""
module contains `to_json_string(...)` function
"""
import json

def to_json_string(my_obj):
    """
    return:
        JSON representation of an object string
    """
    json_dump = json.dumps(my_obj)
    return json_dump
