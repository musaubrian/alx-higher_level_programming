#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    random_list = []
    for index in range(len(my_list)):
        if my_list[index] % 2 == 0:
            random_list.append(True)
        else:
            random_list.append(False)

    return random_list
