#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """Write to a file"""
    with open(filename, 'w', encoding="utf-8") as file:
        text = str(text)
        data_written = file.write(text)
    file.closed

    return data_written
