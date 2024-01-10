#!/usr/bin/python3
""" Module that contains a function that writes to a text file
"""


def write_file(filename="", text=""):
    """Function that writes to a text file
    
    Keyword Arguments:
        filename {str} -- filename (default: {""})
        text {str} -- text to write (default: {""})
        
    Raises:
        Exception: when the file can be opened
        
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
