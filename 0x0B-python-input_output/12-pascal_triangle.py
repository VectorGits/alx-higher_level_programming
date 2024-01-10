#!/usr/bin/python3
"""Module for pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle
    Args:
        n (int): number of rows in triangle
    Returns: list of lists of integers
    """
    trix = []
    rev = []

    for x in range(n):
        res_list = []
        p1 = -1
        p2 = 0
        for y in range(len(rev) + 1):
            if p1 == -1 or p2 == len(rev):
                res_list.append(1)
            else:
                res_list.append(rev[p1] + rev[p2])
            p1 += 1
            p2 += 1

        trix.append(res_list)
        rev = res_list

    return trix
