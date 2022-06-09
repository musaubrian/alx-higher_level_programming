#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = my_list.copy()
    temp = []
    index = 0
    for items in my_new_list:
        if items == search:
            my_new_list[index] = replace
        index += 1

    return my_new_list
