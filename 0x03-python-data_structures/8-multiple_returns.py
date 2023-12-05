#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]

    length = len(sentence)
    res_tuple = (length, first_char)
    return res_tuple
