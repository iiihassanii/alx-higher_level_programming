#!/usr/bin/python3
""" writes an Object to a text file,
using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file,
    using a JSON representation:"""
    with open(filename, "w") as file:
        my_obj_as_list = list(my_obj)
        json.dump(my_obj_as_list, file)
    # file.closed
