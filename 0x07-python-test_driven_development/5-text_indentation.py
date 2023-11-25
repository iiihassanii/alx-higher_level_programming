#!/usr/bin/python3
"""_summary_"""


def text_indentation(text):
    """_summary_

    Args:
        text (str): _description_

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    add_space = True
    new_text = ""
    for i in range(0, len(text)):
        if text[i] not in [" ", '\t']:
            add_space = True
        if add_space:
            new_text += text[i]
        if text[i] in [".", "?", ":"]:
            print(new_text, end="\n\n")
            add_space = False
            new_text = ""
