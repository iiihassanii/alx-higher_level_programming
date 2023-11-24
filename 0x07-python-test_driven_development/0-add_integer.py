#!/usr/bin/python3
"""_summary_"""


def add_integer(a, b=98):
    """_summary_

    Args:
        a (_type_): _description_
        b (int, optional): _description_. Defaults to 98.

    Raises:
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
