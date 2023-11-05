#!/usr/bin/python3
def no_c(my_string):
    _new_string = my_string.translate({ord("c"): None})
    _new_string = my_string.translate({ord("C"): None})
    return _new_string
