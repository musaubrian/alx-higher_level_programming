#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    my_dictionary = a_dictionary.copy()
    for key in my_dictionary:
        my_dictionary[key] *= 2
    return my_dictionary
