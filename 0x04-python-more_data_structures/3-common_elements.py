#!/usr/bin/python3
def common_elements(set_1, set_2):
    if len(set.intersection(set_2)) > 0:
        string = set_1.intersection(set_2)
    return string
