#!/usr/bin/python3
"""_summary_
    """


def append_after(filename="", search_string="", new_string=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        search_string (str, optional): _description_. Defaults to "".
        new_string (str, optional): _description_. Defaults to "".
    """
    text = ""
    with open(filename) as readf:
        for line in readf:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as writef:
        writef.write(text)
