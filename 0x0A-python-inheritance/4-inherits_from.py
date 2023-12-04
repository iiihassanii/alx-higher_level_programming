#!/usr/bin/python3
"""summary"""


def inherits_from(obj, a_class):
    """_summary_

    Args:
            obj (_type_): _description_
            a_class (_type_): _description_
    Return:
    """
    return isinstance(obj, a_class) and type(obj) != a_class
