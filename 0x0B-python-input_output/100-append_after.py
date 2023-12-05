#!/usr/bin/python3
"""text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """

    Args:
        filename (str): The name of the file.
        search_string (str): The string
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as file1:
        for line in file1:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file:
        file.write(text)

