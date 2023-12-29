#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """return dictionary description with simple data structure.

    Args:
        obj: is an instance of a Class

    Returns:
        dictionary
    """
    return obj.__dict__
