#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) <= 123 and ord(char) >= 97:
            char = chr(ord(char) - 32)
        print("{}".format(char), end='')
    print('\n', end='')
