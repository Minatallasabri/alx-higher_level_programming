#!/usr/bin/python3
"""Module for find_peak function"""

def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers."""
    if list_of_integers is None or list_of_integers == []:
        return None
    return max(list_of_integers)
