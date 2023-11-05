#!/usr/bin/python3
def element_at(my_list, idx):
    j = len(my_list) - 1
    if idx < 0 or idx > j:
        return None
    return my_list[idx]
