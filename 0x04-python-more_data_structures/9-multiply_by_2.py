#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cp_dictionary = {}
    for key, value in a_dictionary.items():
        cp_dictionary[key] = value * 2
    return cp_dictionary
