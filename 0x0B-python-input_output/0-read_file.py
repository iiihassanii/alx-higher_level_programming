#!/usr/bin/python3
""" READ FILE"""


def read_file(filename=""):
    """read data from file"""
    with open(filename, 'r', encoding="utf-8") as f:

        read_data = f.read()
        print(read_data, end="")
    f.closed
