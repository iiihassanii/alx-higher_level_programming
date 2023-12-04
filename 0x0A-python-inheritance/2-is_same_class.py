#!/usr/bin/python3
"""summary"""


def is_same_class(obj, a_class):
    """_summary_

    Args:
            obj (_type_): _description_
            a_class (_type_): _description_
    return:
            True if the object is exactly an instance of the specified class ; otherwise False
    """
    return type(obj) == a_class
