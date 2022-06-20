#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        my_new_list = my_list[:x]
        print(''.join(str(s) for s in my_new_list))
        count = 0
        for _ in my_new_list:
            count += 1
        return count
    except IndexError:
        num = my_list[-1:]
        counter = 0
        for _ in my_list:
            counter += 1
        return counter
