#!/usr.bin/python3

def best_score(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is dict:
        return None

    return_value = list(a_ditcionary.keys())[0]
    big_value = a_dictionary[return_value]
    for key, value in a_dictionary.items():
        if value > big:
            big_value = value
            return_value = key
    return return_value
