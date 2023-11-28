#!/usr/bin/python3
"""
    Module containing text indentation function
"""


def text_indentation(text):
    """ Text indentation function

    Args:
        text (str): A string of text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    adnew_space = True
    size = 0
    text = text.strip()
    new_text = ""
    for x in text:
        if x is " " and adnew_space:
            pass
        elif x is "." or x is "?" or x is ":":
            new_text += x + "\n\n"
            adnew_space = True
        else:
            new_text += x
            adnew_space = False
    print(new_text, end='')
