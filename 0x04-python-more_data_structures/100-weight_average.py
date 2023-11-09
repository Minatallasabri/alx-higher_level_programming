#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    dev = 0
    for tup in my_list:
        average += tup[0] * tup[1]
        dev += tup[1]
    return float(average / dev)
