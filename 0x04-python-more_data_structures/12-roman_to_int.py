#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    for x, c in enumerate(roman_string):
        if x != len(roman_string) - 1 and roman_values[c] < roman_values[roman_string[x+1]]:
            total -= roman_values[c]
        else:
            total += roman_values[c]

    return total
