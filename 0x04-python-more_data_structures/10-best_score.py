#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        new_dictionary = sorted(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == new_dictionary[-1]:
                return key
    else:
        return None
