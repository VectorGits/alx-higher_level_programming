#!/usr/bin/python3
def weight_average(my_list=[]):
    # Check if my_list is empty
    if my_list == []:
        return (0)
    # Calculate the weighted average
    total_weight = 0
    total_weighted_score = 0
    for score, weight in my_list:
        total_weight += weight
        total_weighted_score += (score * weight)
    weighted_average = total_weighted_score / total_weight
    return (weighted_average)
