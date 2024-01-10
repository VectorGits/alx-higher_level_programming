#!/usr/bin/python3
"""Module for pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle
    Args:
        n (int): number of rows in triangle
    Returns: list of lists of integers
    """
    if n <= 0:
        return[]
    triangle = []
    for x in range(n):
        row = [1] * (x + 1)
    for y in range(1, x):
        row[y] = triangle[x - 1][y - 1] + triangle[x - 1][y]
    triangle.append(row)
    return triangle
