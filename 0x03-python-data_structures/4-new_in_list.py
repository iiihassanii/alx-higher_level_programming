#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpmy_list = my_list.copy()

    if idx < 0 or idx > len(cpmy_list) - 1:
        return cpmy_list
    cpmy_list[idx] = element
    return cpmy_list
