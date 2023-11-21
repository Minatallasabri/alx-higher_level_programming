#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        safun = fct(*args)
    except Exception as Exc:
        print("Exception: {}".format(Exc), file=sys.stderr)
        return None
    else:
        return safun
