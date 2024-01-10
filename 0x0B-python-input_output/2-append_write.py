#!/usr/bin/python3
"""Module that contains a function that appends to a text file"""


def append_write(filename="", text=""):
    """Function that appends to a text file

    Keyword Arguments:
        filename {str} -- filename (default: {""})
        text {str} -- text to append (default: {""})

    Raises:
        Exception: when the file can be opened

    """

    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
