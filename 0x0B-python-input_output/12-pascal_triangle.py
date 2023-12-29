#!/usr/bin/python3
"""Pascal Tringle"""


def pascal_triangle(n):
    """The main function of pascal triangle"""
    if n <= 0:
        return []

    pastring = [[1]]

    while len(pastring) != n:
        tringle = pastring[-1]
        tmp = [1]
        for index in range(len(tringle) - 1):
            tmp.append(tringle[index] + tringle[index + 1])
        tmp.append(1)
        pastring.append(tmp)
    return pastring
