#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for k, v in a_dictionary.items():
            a = k
            b = v
            break
        for k, v in a_dictionary.items():
            if b < v:
                a = k
                b = v
        return(a)
    return
