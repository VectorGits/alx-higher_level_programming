#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    res_list = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return res_list
