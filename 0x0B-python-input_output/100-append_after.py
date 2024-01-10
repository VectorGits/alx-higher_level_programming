#!/usr/bin/python3
"""Module for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a
    specific string
    Args:
        filename (str): name of file
        search_string (str): string to search for
        new_string (str): string to append
    """
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
