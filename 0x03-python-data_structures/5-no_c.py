#!/usr/bin/python3

def no_c(my_string):
    string_to_edit = list(my_string)
    for character in string_to_edit:
        if character == 'c' or character == 'C':
            string_to_edit.remove(character)

    string_to_edit = ''.join([str(character) for character in string_to_edit])
    return string_to_edit
